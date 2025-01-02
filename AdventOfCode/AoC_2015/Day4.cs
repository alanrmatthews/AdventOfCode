namespace AoC_2015;

public class Day4(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        return FindHash("00000");
    }

    public override string Part2()
    {
        return FindHash("000000");
    }

    private string FindHash(string prefix)
    {
        var line = File.ReadLines(InputFile).First();
        int i = 0;
        var lineBytes = System.Text.Encoding.UTF8.GetBytes(line);

        var byte2Max = 0x10;
        if (prefix.Length == 6)
            byte2Max = 0x1;

        while (true)
        {
            var iBytes = System.Text.Encoding.UTF8.GetBytes(i.ToString());
            var hashBytes = System.Security.Cryptography.MD5.HashData([.. lineBytes, .. iBytes]);
            if (hashBytes[0] == 0 && hashBytes[1] == 0 && hashBytes[2] < byte2Max)
                return i.ToString();
            i++;
        }
    }
}
