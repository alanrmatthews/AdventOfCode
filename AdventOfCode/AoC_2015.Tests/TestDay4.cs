namespace AoC_2015.Tests;

[TestClass]
public class TestDay4 : Utilities.BaseTest
{
    protected override Day4 getDay() => new("../../../inputs/day4.txt");
    protected override string ExpectedP1() => "282749";
    protected override string ExpectedP2() => "9962624";
}

