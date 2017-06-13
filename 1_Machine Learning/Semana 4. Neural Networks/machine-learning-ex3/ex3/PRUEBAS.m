a = [1;2;1;1;1;1];
b = [2;2;2;2;2;2];

c = a.*b;
n  = length(a);  %numero de features
c = ones(n,1)