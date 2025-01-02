using Utilities;

namespace AoC_2015.Tests;

[TestClass]
public abstract class BaseTest
{
    [TestMethod]
    public void TestPart1()
    {
        Assert.AreEqual(ExpectedP1(), getDay().Part1());
    }

    [TestMethod]
    public void TestPart2()
    {
        Assert.AreEqual(ExpectedP2(), getDay().Part2());
    }

    protected abstract BaseDay getDay();
    protected abstract string ExpectedP1();
    protected abstract string ExpectedP2();
}
