using System.Text.RegularExpressions;

namespace AoC_2015;

public class Day2(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        int sum = 0;
        foreach (var line in File.ReadLines(InputFile))
            sum += WrappingPaperNeeded(line);

        return sum.ToString();
    }

    public override string Part2()
    {
        int sum = 0;
        foreach (var line in File.ReadLines(InputFile))
            sum += RibbonNeeded(line);

        return sum.ToString();
    }

    private int WrappingPaperNeeded(string line)
    {
        var dimensions = GetDimensions(line);
        (int l, int w, int h) = (dimensions[0], dimensions[1], dimensions[2]);

        var sides = new List<int> { l * w, w * h, h * l };
        return (sides.Sum() * 2) + sides.Min();
    }

    private int RibbonNeeded(string line)
    {
        var dimensions = GetDimensions(line);
        (int l, int w, int h) = (dimensions[0], dimensions[1], dimensions[2]);
        var shortest = dimensions.OrderBy(d => d).Take(2).ToList();
        return shortest[0] + shortest[0] + shortest[1] + shortest[1] + (l * w * h);
    }

    private List<int> GetDimensions(string dimensions)
    {
        var digits = Regex.Matches(dimensions, @"\d+");
        return digits.Select(d => int.Parse(d.Value)).ToList();
    }
}
