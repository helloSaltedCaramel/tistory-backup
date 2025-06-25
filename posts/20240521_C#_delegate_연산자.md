# C# delegate 연산자

*발행: Tue, 21 May 2024 15:44:25 +0900*

---

<pre class="csharp" id="code_1716273606473"><code>func&lt;int, int, int &gt; sum = delegate (int a, int b)
{
	return a + b;
};

Console.WriteLine(sum(3,4));

7</code></pre>