# [UART] RX &amp; TX

*발행: Thu, 26 Jun 2025 10:47:29 +0900*

---

<p>RX와 TX는 시리얼 통신(Serial Communication) 또는 UART(Universal Asynchronous Receiver/Transmitter) 통신에서 자주 등장하는 기본 개념 입니다. 각각 다음과 같은 뜻을 가집니다.</p>
<p>&nbsp;</p>
<h4><b>RX/ TX란?</b></h4>
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>약어</td>
<td>의미</td>
<td>역할</td>
</tr>
<tr>
<td>TX</td>
<td>Transmit (송신)</td>
<td>데이터를 보내는 역할</td>
</tr>
<tr>
<td>RX</td>
<td>Receive (수신)</td>
<td>데이터를 받는 역할</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4 style="color: #000000; text-align: start;"><b>기본 동작 개념</b></h4>
<p>시리얼 통신에서는 최소한 두 장치 (PC &lt;-&gt; MCU)가 연결됩니다. 이때 다음과 같이 연결됩니다.</p>
<pre class="bash" id="code_1750902390610"><code>PC TX ─────────▶ MCU RX   (PC가 데이터를 보냄 &rarr; MCU가 받음)
PC RX ◀───────── MCU TX   (MCU가 데이터를 보냄 &rarr; PC가 받음)</code></pre>
<p>즉, 한쪽의 TX는 상대방의 RX에 연결되어야 통신이 가능합니다.&nbsp;</p>