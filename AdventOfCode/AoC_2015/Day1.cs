namespace AoC_2015;

public class Day1(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        var line = File.ReadLines(InputFile).First();
        return line.Select(c => c == '(' ? 1 : -1).Sum().ToString();
    }

    public override string Part2()
    {
        var line = File.ReadLines(InputFile).First();
        var counter = 0;
        for (int i = 0; i < line.Length; i++)
        {
            counter += line[i] == '(' ? 1 : -1;
            if (counter == -1)
            {
                return (i + 1).ToString();
            }
        }

        return "ERROR";
    }
}
