#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <string.h>
#include <cmath>
#include <iomanip>

using namespace std;
#define CASE 100
#define WAVE_NUM 32
#define ONU_NUM 64 * 4
#define DAY 30
#define CAPACITY 3.0 * 4
#define EVENT DAY * 24 * CASE
#define MAX_PERIOD 7
#define MAX_RESERVATION 5

struct ONU
{
	double traffic;
    int No_onu;
	int No_wavelength;
};

bool cmp(ONU a, ONU b);
void First_fit(vector<ONU> onu_vector, int *wavelength, double *burden);
void Save_parameter(int *wavelength, double *burden, fstream &file_wave, fstream &file_burden);
void Process(fstream &input_file, fstream &output_file);
void Process_res(fstream &input_file, fstream &output_file);
void Best_fit(vector<ONU> onu, int *wavelength, double *burden);


int main()
{   
    fstream infile_traffic;                             // input data
    fstream file_wavelength, file_burden;               // First fit 
    fstream file_binpack;                               // bin packing result
    fstream file_reserve;                               // reservation result

    int wavelength[WAVE_NUM];
    double burden[WAVE_NUM];

    map<int, double> onu_map;
    vector<ONU> onu_vector;
	ONU temp;

    //******************** input data
    infile_traffic.open("traffic_data.txt", fstream::in);

    //******************** First fit
    file_wavelength.open("wavelength.txt", fstream::out);
    file_burden.open("burden.txt", fstream::out);
    

    for (int k=0; k<EVENT; k++)
    {
        for (int i=0; i<ONU_NUM; i++)
        {
            infile_traffic >> temp.traffic;
            onu_vector.push_back(temp);
        }

        sort(onu_vector.begin(), onu_vector.end(), cmp);

        First_fit(onu_vector, wavelength, burden);
        Save_parameter(wavelength, burden, file_wavelength, file_burden);
        onu_vector.clear();
    }
    

    infile_traffic.close();
    file_wavelength.close(), file_burden.close();
    
    //***************** bin-packing, First fit process
    file_wavelength.open("wavelength.txt", fstream::in);
    file_binpack.open("binpack.txt", fstream::out);
    Process(file_wavelength, file_binpack);
    file_wavelength.close();
    file_binpack.close();


    //***************** reservation, First fit process
    cout << "first fit" << endl;
    file_binpack.open("binpack.txt", fstream::in);
    file_reserve.open("reserve.txt", fstream::out);
    Process_res(file_binpack, file_reserve);
    file_binpack.close();
    file_reserve.close();
    
	return 0;
}


bool cmp(ONU a, ONU b)    //sort in decreasing
{
	if(a.traffic > b.traffic)
		return true;
	else
		return false;
}

//*****************  First fit decreasing algorithm
void First_fit(vector<ONU> onu_vector, int *wavelength, double *burden)
{   
    //**************** initialization 
        
    for (int i=0; i<WAVE_NUM; i++)
    {
        burden[i] = 0.0;                // burden of wavelength i is zero
        wavelength[i] = 0;              // wavelength i is not use
    }
    
    //****************** first fit algorithm
    bool pack_all = false;
    for(int i=0; i<ONU_NUM; i++)
    {   
        pack_all = false;
    	for (int j=0; j<WAVE_NUM; j++)
    	{
    		if (onu_vector[i].traffic + burden[j] <= CAPACITY)
    		{
    			wavelength[j] = 1;
    			burden[j] += onu_vector[i].traffic;
                pack_all = true;
    			break;
    		}
    	}
        if (!pack_all)
        {
            cout << "traffic out of bound! generate new traffic" << endl;
            break;
        }
    }
}
//*****************  Best fit decreasing algorithm
void Best_fit(vector<ONU> onu, int *wavelength, double *burden)
{
    //**************** initialization 

    for (int i=0; i<WAVE_NUM; i++)
    {
        burden[i] = 0.0;                // burden of wavelength i is zero
        wavelength[i] = 0;              // wavelength i is not use
    }
    
    //****************** best fit algorithm
    double current_burden = 0.0;
    int index = 0, used_wave = 0;
    bool is_found = false;
    bool pack_all = false;
    for(int i=0; i<ONU_NUM; i++)
    {   
        current_burden = 0, index = 0, is_found = false;
        for (int j=0; j<used_wave; j++)
        {
            if (onu[i].traffic + burden[j] <= CAPACITY && current_burden < burden[j])
            {
                current_burden = burden[j];
                index = j;
                if (!is_found)
                    is_found = true;
                pack_all = true;
            }
        }
        
        if (!is_found)
        {
            index = used_wave;
            used_wave++;
        }

        if (!pack_all)
        {
            cout << "traffic out of bound! generate new traffic" << endl;
            break;
        }

        wavelength[index] = 1;
        burden[index] += onu[i].traffic;
    }
}

void Save_parameter(int *wavelength, double *burden, fstream &file_wave, fstream &file_burden)
{   
	for (int i=0; i<WAVE_NUM; i++)
	{
		file_wave << wavelength[i] << '\t';
	}
    file_wave << endl;
    
    for (int i=0; i<WAVE_NUM; i++)
    {
        file_burden << burden[i] << '\t';
    }
    file_burden << endl;

}

void Process(fstream &input_file, fstream &output_file)
{ 
    int sum1 = 0, sum2 = 0, total_onoff = 0;
    int temp = 0, diff = 0;
    int total_wavelength = 0;
    
    for (int i=0; i<EVENT; i++)
    {
        for (int j=0; j<WAVE_NUM; j++)
        {
            input_file >> temp;
            sum2 += temp;
        }

        diff = abs(sum2 - sum1);
        output_file << sum2 << '\t' << diff << endl;
        total_onoff += diff;       
        total_wavelength += sum2;

        sum1 = sum2;
        sum2 = 0;
    }
    output_file << "total number of used wavelength" << '\t' << total_wavelength << endl;
    output_file << "total number of on-off" << '\t' << total_onoff << endl;
	cout << "bin-packing" << '\t' << total_wavelength << '\t' << total_onoff << endl;
}

void Process_res(fstream &input_file, fstream &output_file)
{
    int use[EVENT], new_use[EVENT];
    int a = 0, b = 0;
    for (int i=0; i<EVENT; i++)
    {
        input_file >> a >> b;
        use[i] = a;
        new_use[i] = a;
    }

    int sum1 = 0, sum2 = 0, diff = 0;
    int total_onoff = 0, total_wavelength = 0;
    int index = 0, resource = 0;
    
    for (int max_resource = 1; max_resource <= MAX_RESERVATION; max_resource++)
    {
        for (int period = 1; period <= MAX_PERIOD; period++)
        {   
            index = 0, sum1 = 0, sum2 = 0;
            while (index+period < EVENT)
            {   
                int t = period;
                sum2 = use[index];
                new_use[index] = use[index];

                if (sum1 > sum2)
                {   
                    if (sum1 - sum2 >= max_resource)
                    {   
                        resource = max_resource;  
                        new_use[index] += resource; 
                    }
                    else
                    {
                        resource = sum1 - sum2;
                        new_use[index] += resource;  
                    }
                        
                    for (int i=1; i<period; i++)
                    {   
                        new_use[i+index] = use[i+index];

                        if (use[i+index] > use[i+index-1])    // reserved resource is used
                        {
                            resource = resource - (use[i+index] - use[i+index-1]);
                            if (resource <= 0)                // reserved resource is used up
                            {
                                t = i;
                                break;
                            }
                            else
                            {
                                new_use[i+index] += resource;
                            }
                        }
                        else
                        {   
                            if (use[i+index-1] - use[i+index] + resource >= max_resource)
                            {     
                                resource = max_resource;
                                new_use[i+index] += resource;        // reserved resource is not used up
                            }                                   
                            else
                            {
                                resource += use[i+index-1] - use[i+index];
                                new_use[i+index] += resource;
                            }
                        }
                    }

                    if(t == period)
                    {   
                        new_use[index+period] = use[index+period];
                    }

                    sum1 = use[index + t];
                    index += t + 1;
                }
                else
                {   
                    sum1 = use[index];
                    index++;
                }
            }

            sum1 = 0, sum2 = 0, diff = 0, total_onoff = 0, total_wavelength = 0;
            for (int i=0; i<EVENT; i++)
            {
                sum2 = new_use[i];
                diff = abs(sum2 - sum1);

                sum1 = sum2;
                total_onoff += diff;
                total_wavelength += sum2;
                output_file << sum2 << '\t' << diff << endl;
            }

            //output_file << "lamda = " << max_resource << '\t' << "period = " << period << endl;
            //output_file << "total number of used wavelength" << '\t' << total_wavelength << endl;
            //output_file << "total number of on-off" << '\t' << total_onoff << endl;
            //output_file << endl;
            cout << "lamda = " << max_resource << '\t' << "period = " << period << '\t' << total_wavelength << '\t' << total_onoff << endl;
        }
        cout << endl;
    }
}
