namespace AoC_2015.Tests;

[TestClass]
public class TestDay5Sample : Utilities.BaseTest
{
    protected override Day5 getDay() => new("../../../inputs/day5_sample.txt");
    protected override string ExpectedP1() => "2";
    protected override string ExpectedP2() => "0";
}

[TestClass]
public class TestDay5 : Utilities.BaseTest
{
    protected override Day5 getDay() => new("../../../inputs/day5.txt");
    protected override string ExpectedP1() => "255";
    protected override string ExpectedP2() => "55";
}

