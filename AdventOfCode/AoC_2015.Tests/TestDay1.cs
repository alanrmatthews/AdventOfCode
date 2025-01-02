namespace AoC_2015.Tests;

[TestClass]
public class TestDay1Sample : Utilities.BaseTest
{
    protected override Day1 getDay() => new("../../../inputs/day1_sample.txt");
    protected override string ExpectedP1() => "-3";
    protected override string ExpectedP2() => "1";
}

[TestClass]
public class TestDay1 : Utilities.BaseTest
{
    protected override Day1 getDay() => new("../../../inputs/day1.txt");
    protected override string ExpectedP1() => "232";
    protected override string ExpectedP2() => "1783";
}

