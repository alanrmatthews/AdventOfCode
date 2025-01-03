namespace AoC_2015.Tests;

[TestClass]
public class TestDay3 : Utilities.BaseTest
{
    protected override Day3 getDay() => new("../../../inputs/day3.txt");
    protected override string ExpectedP1() => "2572";
    protected override string ExpectedP2() => "2631";
}

