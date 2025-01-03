using System.Text.RegularExpressions;

namespace AoC_2015;

public class Day5(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        var lines = File.ReadLines(InputFile);
        return lines.Select(l => IsNice(l) ? 1 : 0).Sum().ToString();
    }

    public override string Part2()
    {
        var lines = File.ReadLines(InputFile);
        return lines.Select(l => IsNice2(l) ? 1 : 0).Sum().ToString();
    }

    private static bool IsNice(string line)
    {
        int vowels = 0;
        bool doubles = false;

        for (int i = 0; i < line.Length; i++)
        {
            if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' || line[i] == 'o' || line[i] == 'u')
                vowels++;

            if (i > 0)
            {
                if (line[i] == 'b' && line[i - 1] == 'a' || line[i] == 'd' && line[i - 1] == 'c' ||
                    line[i] == 'q' && line[i - 1] == 'p' || line[i] == 'y' && line[i - 1] == 'x')
                {
                    return false;
                }

                if (line[i] == line[i - 1])
                    doubles = true;
            }
        }

        return doubles && vowels >= 3;
    }

    private static bool IsNice2(string line)
    {
        var pairPattern = new Regex(@"(..).*\1");
        var repeatPattern = new Regex(@"(.).\1");

        return pairPattern.IsMatch(line) && repeatPattern.IsMatch(line);
    }
}
