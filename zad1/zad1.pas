program RandomNumbersAndSort;

uses
  SysUtils;

const
  size = 50;

type
  numberArray = array[1..size] of Integer;

procedure printArr(arr: numberArray);
var
  i: Integer;
begin
  for i := 1 to size do
    Write(arr[i], ' ');
  Writeln;
end;

procedure genRandomNumbers(var arr: numberArray);
var
  i: Integer;
begin
  Randomize;
  for i := 1 to size do
    arr[i] := Random(101);
end;

procedure bubbleSort(var arr: numberArray);
var
  i, j, temp: Integer;
begin
  for i := 1 to size - 1 do
    for j := 1 to size - i do
      if arr[j] > arr[j + 1] then
      begin
        temp := arr[j];
        arr[j] := arr[j + 1];
        arr[j + 1] := temp;
      end;
end;

var
  numbers: numberArray;

begin
  genRandomNumbers(numbers);
  Writeln('Numbers before sort:');
  printArr(numbers);

  bubbleSort(numbers);
  Writeln('Numbers after sort:');
  printArr(numbers);
end.