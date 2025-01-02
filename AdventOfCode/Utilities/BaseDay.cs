namespace Utilities;

public abstract class BaseDay(string File)
{
    protected string InputFile = File;

    public abstract string Part1();
    public abstract string Part2();
}
