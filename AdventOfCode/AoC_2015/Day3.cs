namespace AoC_2015;

public class Day3(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        var line = File.ReadLines(InputFile).First();
        var pos = (x: 0, y: 0);
        var visited = new HashSet<(int, int)>() { pos };
        foreach (var c in line)
        {
            pos = VisitHouse(c, pos, visited);
        }

        return visited.Count.ToString();
    }

    public override string Part2()
    {
        var line = File.ReadLines(InputFile).First();
        var santaPos = (x: 0, y: 0);
        var roboPos = (x: 0, y: 0);
        var visited = new HashSet<(int, int)>() { santaPos };

        for (int i = 0; i < line.Length; i += 2)
        {
            santaPos = VisitHouse(line[i], santaPos, visited);
            roboPos = VisitHouse(line[i + 1], roboPos, visited);
        }

        return visited.Count.ToString();
    }

    private static (int x, int y) VisitHouse(char c, (int x, int y) pos, HashSet<(int, int)> visited)
    {
        switch (c)
        {
            case '^':
                pos.x++;
                break;
            case '>':
                pos.y++;
                break;
            case 'v':
                pos.x--;
                break;
            case '<':
                pos.y--;
                break;
        }

        visited.Add(pos);
        return pos;
    }
}
