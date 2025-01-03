namespace AoC_2015.Tests;

[TestClass]
public class TestDay2 : Utilities.BaseTest
{
    protected override Day2 getDay() => new("../../../inputs/day2.txt");
    protected override string ExpectedP1() => "1598415";
    protected override string ExpectedP2() => "3812909";
}

