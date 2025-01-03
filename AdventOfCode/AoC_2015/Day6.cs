using System.Text.RegularExpressions;

namespace AoC_2015;

public class Day6(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        var lightsOn = new bool[1000, 1000];
        var instructions = new Regex(@"(.*) (\d+),(\d+) through (\d+),(\d+)", RegexOptions.Compiled);

        foreach (var line in File.ReadLines(InputFile))
        {
            var match = instructions.Match(line);
            var instruction = match.Groups[1].Value;
            var x1 = int.Parse(match.Groups[2].Value);
            var y1 = int.Parse(match.Groups[3].Value);
            var x2 = int.Parse(match.Groups[4].Value);
            var y2 = int.Parse(match.Groups[5].Value);

            if (instruction == "turn on")
                TurnOnLights(lightsOn, x1, y1, x2, y2);
            else if (instruction == "turn off")
                TurnOffLights(lightsOn, x1, y1, x2, y2);
            else if (instruction == "toggle")
                ToggleLights(lightsOn, x1, y1, x2, y2);
        }

        return lightsOn.Cast<bool>().Count(x => x).ToString();
    }

    public override string Part2()
    {
        var lightsOn = new int[1000, 1000];
        var instructions = new Regex(@"(.*) (\d+),(\d+) through (\d+),(\d+)", RegexOptions.Compiled);

        foreach (var line in File.ReadLines(InputFile))
        {
            var match = instructions.Match(line);
            var instruction = match.Groups[1].Value;
            var x1 = int.Parse(match.Groups[2].Value);
            var y1 = int.Parse(match.Groups[3].Value);
            var x2 = int.Parse(match.Groups[4].Value);
            var y2 = int.Parse(match.Groups[5].Value);

            if (instruction == "turn on")
                TurnOnLights(lightsOn, x1, y1, x2, y2);
            else if (instruction == "turn off")
                TurnOffLights(lightsOn, x1, y1, x2, y2);
            else if (instruction == "toggle")
                ToggleLights(lightsOn, x1, y1, x2, y2);
        }

        return lightsOn.Cast<int>().Sum().ToString();
    }

    private static void TurnOnLights(bool[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y] = true;
            }
        }
    }

    private static void TurnOffLights(bool[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y] = false;
            }
        }
    }

    private static void ToggleLights(bool[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y] = !lightsOn[x, y];
            }
        }
    }

    private static void TurnOnLights(int[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y]++;
            }
        }
    }

    private static void TurnOffLights(int[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y] = Math.Max(0, lightsOn[x, y] - 1);
            }
        }
    }

    private static void ToggleLights(int[,] lightsOn, int x1, int y1, int x2, int y2)
    {
        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                lightsOn[x, y] += 2;
            }
        }
    }
}
