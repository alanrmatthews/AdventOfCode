namespace AoC_2015.Tests;

[TestClass]
public class TestDay5 : Utilities.BaseTest
{
    protected override Day5 getDay() => new("../../../inputs/day5.txt");
    protected override string ExpectedP1() => "255";
    protected override string ExpectedP2() => "55";
}

