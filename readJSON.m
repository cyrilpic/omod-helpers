function data = readJSON(fname)
%readJSON - read JSON data from file named fname
%
% Syntax: data = readJSON(fname)
%
data = jsondecode(fileread(fname));
end
