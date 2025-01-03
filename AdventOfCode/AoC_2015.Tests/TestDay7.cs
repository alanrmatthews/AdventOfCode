namespace AoC_2015.Tests;

[TestClass]
public class TestDay7 : Utilities.BaseTest
{
    protected override Day7 getDay() => new("../../../inputs/day7.txt");
    protected override string ExpectedP1() => "16076";
    protected override string ExpectedP2() => "2797";
}

