clear all, close all, clc

y_business = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.40, 0.60, 1.00, 1.00, 1.00, 1.00, ...
     1.00, 1.00, 1.00, 1.00, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40];
y_residence = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, ...
     0.40, 0.40, 0.40, 0.60, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00];

%set(gca, 'XTickLabel', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', ...
%    '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'});

category_temp = 0;    % 0 represents only business traffic, 1 represents only resident traffic, 2 represents both
standard_a = 0.8, standard_b = 0.4;
onu_a = 0.8, onu_b = 0.4;
case_num = 100;
day_num = 30, onu_num = 64 * 4;
event = day_num .* 24 .* case_num;


y_standard_business = zeros(1,24);
y_standard_residence = zeros(1,24);

%{
figure
subplot(2,2,1);   % plot business traffic
bar(y_business, 0.5)
grid on
axis([0,25, 0, 1.8]);

subplot(2,2,2);   % plot resident traffic
bar(y_residence, 0.5)
grid on
axis([0,25, 0, 1.8]);

for n = 1:24
    y_standard_business(n) = y_business(n) .* (standard_a + standard_b * rand(1,1));
end
subplot(2,2,3);   % plot business standard traffic
bar(y_standard_business, 0.5)
grid on
axis([0,25, 0, 1.8]);

for n = 1:24
    y_standard_residence(n) = y_residence(n) .* (standard_a + standard_b * rand(1,1));
end
subplot(2,2,4);   % plot residence standard traffic
bar(y_standard_residence, 0.5)
grid on
axis([0,25, 0, 1.8]);

figure                % plot final business traffic
for i=1:4
    for n = 1:24
        y_test(n) = y_standard_business(n) .* (onu_a + onu_b * rand(1,1)); % fluctuation 1 - 1.4
    end
    subplot(2,2,i);
    bar(y_test, 0.5)
    grid on
    axis([0,25, 0, 1.8]);
end

figure                % plot final resident traffic
for i=1:4
    for n = 1:24
        y_test(n) = y_standard_residence(n) .* (onu_a + onu_b * rand(1,1)); % fluctuation 1 - 1.4
    end
    subplot(2,2,i);
    bar(y_test, 0.5)
    grid on
    axis([0,25, 0, 1.8]);
end
%}

y_final = zeros(1,24);
A = zeros(event, onu_num);

if category_temp == 0
    for k = 1:case_num
        disp(k)

        for m = 1:24
            y_standard_business(m) = y_business(m) .* (standard_a + standard_b * rand(1,1));
        end

        for i = 1:onu_num
            for j = 1:day_num
                for n = 1:24
                    y_final(n) = y_standard_business(n) .* (onu_a + onu_b * rand(1,1));
                    A((k-1)*720 + (j-1)*24 + n, i) = y_final(n);
                end
            end
        end

    end
elseif category_temp == 1
    for k = 1:case_num
        disp(k)

        for m = 1:24
            y_standard_residence(m) = y_residence(m) .* (standard_a + standard_b * rand(1,1));
        end

        for i = 1:onu_num
            for j = 1:day_num
                for n = 1:24
                    y_final(n) = y_standard_residence(n) .* (onu_a + onu_b * rand(1,1));
                    A((k-1)*720 + (j-1)*24 + n, i) = y_final(n);
                end
            end
        end

    end
else
    for k = 1:case_num
        disp(k)

        for m = 1:24
            y_standard_business(m) = y_business(m) .* (standard_a + standard_b * rand(1,1));
            y_standard_residence(m) = y_residence(m) .* (standard_a + standard_b * rand(1,1));
        end

        for i = 1:onu_num / 2
            for j = 1:day_num
                for n = 1:24
                    y_final(n) = y_standard_business(n) .* (onu_a + onu_b * rand(1,1));
                    A((k-1)*720 + (j-1)*24 + n, i) = y_final(n);
                end
            end
        end

        for i = onu_num / 2 + 1:onu_num
            for j = 1:day_num
                for n = 1:24
                    y_final(n) = y_standard_residence(n) .* (onu_a + onu_b * rand(1,1));
                    A((k-1)*720 + (j-1)*24 + n, i) = y_final(n);
                end
            end
        end

    end
end
    

dlmwrite('traffic_data.txt', A, 'delimiter', '\t', 'precision', '%.3f', 'newline', 'pc');

