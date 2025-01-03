using System.Text.RegularExpressions;

namespace AoC_2015;

public class Day7(string Input) : Utilities.BaseDay(Input)
{
    public override string Part1()
    {
        var wiring = SetupWiring();
        return wiring["a"].GetValue(wiring).ToString();
    }

    public override string Part2()
    {
        var Part1WireA = ushort.Parse(Part1());
        var wiring = SetupWiring();
        wiring["b"].OverrideValue(Part1WireA);
        return wiring["a"].GetValue(wiring).ToString();
    }

    private Dictionary<string, Wire> SetupWiring()
    {
        var wiring = new Dictionary<string, Wire>();
        var instructions = new Regex(@"(.*) -> (.*)", RegexOptions.Compiled);

        foreach (var line in File.ReadLines(InputFile))
        {
            var match = instructions.Match(line);
            var operation = match.Groups[1].Value;
            var wireName = match.Groups[2].Value;

            var wire = new Wire(wireName, operation);
            wiring[wireName] = wire;
        }

        return wiring;
    }

    private class Wire
    {
        public string Name { get; }
        public string Operation { get; }

        private ushort Value;
        private bool HasValue;

        public Wire(string name, string operation)
        {
            Name = name;
            Operation = operation;
            HasValue = false;
            Value = 0;
        }

        public void OverrideValue(ushort value)
        {
            Value = value;
            HasValue = true;
        }

        public ushort GetValue(Dictionary<string, Wire> wiring)
        {
            if (!HasValue)
            {
                var ops = Operation.Split(' ');

                // 1 Value is assignment
                if (ops.Length == 1)
                {
                    var op1 = ushort.TryParse(ops[0], out var x) ? x : wiring[ops[0]].GetValue(wiring);
                    Value = op1;
                }
                // 2 Values is NOT
                else if (ops.Length == 2)
                {
                    Value = (ushort)~wiring[ops[1]].GetValue(wiring);
                }
                else
                {
                    var op1 = ushort.TryParse(ops[0], out var x) ? x : wiring[ops[0]].GetValue(wiring);
                    var op2 = ushort.TryParse(ops[2], out var y) ? y : wiring[ops[2]].GetValue(wiring);

                    Value = ops[1] switch
                    {
                        "AND" => (ushort)(op1 & op2),
                        "OR" => (ushort)(op1 | op2),
                        "LSHIFT" => (ushort)(op1 << op2),
                        "RSHIFT" => (ushort)(op1 >> op2),
                        _ => throw new InvalidOperationException()
                    };
                }

                HasValue = true;
            }

            return Value;

        }
    }
}
