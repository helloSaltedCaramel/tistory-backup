# StackPanel

*발행: Wed, 25 Jun 2025 15:27:54 +0900*

---

<p>StackPanel 은 WPF에서 자주 사용되는 레이아웃 컨트롤 중 하나로, 자식 요소들을 일렬로 나열하는 방식으로 배치하는 컨트롤이빈다.&nbsp;</p>
<p>쉬StackPanel 은 WPF에서 자주 사용되는 레이아웃 컨트롤 중 하나로, 자식 요소들을 일렬로 나열하는 방식으로 배치하는 컨트롤이빈다.&nbsp;</p>
<p>&nbsp;</p>
<p>&gt; StackPanel 안에 있는 요소들은 위에서 아래로 또는 왼쪽에서 오른쪽으로 쌓이듯이 정렬됩니다.</p>
<p>&nbsp;</p>
<h4><b>기본 개념</b></h4>
<p>StackPanel은 자식 요소들을 <b>수직 또는 수평 방향</b>으로 배치합니다.</p>
<pre class="bash" id="code_1750831319078"><code>&lt;StackPanel Orientation="Vertical"&gt;
	&lt;Button Content="버튼 1"/&gt;
	&lt;Button Content="버튼 2"/&gt;
&lt;/StackPanel&gt;</code></pre>
<p>이렇게 하면 버튼들이 <b>위에서 아래로</b> 쌓입니다.</p>
<p>&nbsp;</p>
<h4 style="color: #000000; text-align: start;"><b>주요 속성</b></h4>
<p>Orientation</p>
<p>: StackPanel의 방향을 지정합니다.&nbsp;</p>
<p>&nbsp;</p>
<p>값설명</p>
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>값</td>
<td>설명</td>
</tr>
<tr>
<td style="width: 25.6977%;">Vertical</td>
<td style="width: 74.3023%;">위&nbsp; &gt; 아래로 정렬 (기본값)</td>
</tr>
<tr>
<td style="width: 25.6977%;">Horizontal</td>
<td style="width: 74.3023%;">왼쪽 &gt; 오른쪽으로 정렬</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4 style="color: #000000; text-align: start;"><b>사용 예시</b></h4>
<pre class="bash" id="code_1750832808027"><code>수직 배치 (기본)
&lt;StackPanel&gt;
    &lt;TextBlock Text="로그인" FontSize="18"/&gt;
    &lt;TextBox PlaceholderText="아이디"/&gt;
    &lt;PasswordBox/&gt;
    &lt;Button Content="로그인"/&gt;
&lt;/StackPanel&gt;</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<pre class="bash" id="code_1750832820124"><code>수평 배치
&lt;StackPanel Orientation="Horizontal"&gt;
    &lt;Button Content="&larr;" /&gt;
    &lt;TextBlock Text="1 / 10" Margin="5"/&gt;
    &lt;Button Content="&rarr;" /&gt;
&lt;/StackPanel&gt;</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>StackPanel vs Grid vs DockPanel 차이</h2>
<div>
<p>&nbsp;</p>
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>레이아웃</td>
<td>특징</td>
<td>대표 사용 예</td>
</tr>
<tr>
<td><b>StackPanel</b></td>
<td>한 방향으로 쌓기 (간단함)</td>
<td>버튼 그룹, 툴바</td>
</tr>
<tr>
<td><b>Grid</b></td>
<td>행과 열 지정해서 정밀하게 배치</td>
<td>폼, 다단 UI</td>
</tr>
<tr>
<td><b>DockPanel</b></td>
<td>컨트롤을 상/하/좌/우로 배치, 나머지 채움</td>
<td>전체 창 레이아웃</td>
</tr>
</tbody>
</table>
</div>