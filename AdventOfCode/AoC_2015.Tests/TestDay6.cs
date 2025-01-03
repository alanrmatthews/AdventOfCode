namespace AoC_2015.Tests;

[TestClass]
public class TestDay6 : Utilities.BaseTest
{
    protected override Day6 getDay() => new("../../../inputs/day6.txt");
    protected override string ExpectedP1() => "377891";
    protected override string ExpectedP2() => "14110788";
}

