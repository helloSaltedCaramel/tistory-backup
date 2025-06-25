# Error : Void methods cannot return a value

*발행: Fri, 24 Dec 2021 17:45:04 +0900*

---

<p>&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="360" src="https://blog.kakaocdn.net/dn/drkIQI/btroPI3hTS2/HU6cEOKMNEeocWkM1p76Kk/img.png" width="1096" /></span></figure>
</p>
<p><b>error 메세지</b></p>
<p>SEVERE:&nbsp;웹&nbsp;애플리케이션&nbsp;[/mybatis03]&nbsp;내의&nbsp;서블릿&nbsp;[appServlet]이(가)&nbsp;load()&nbsp;예외를&nbsp;발생시켰습니다.<br />java.lang.Error:&nbsp;Unresolved&nbsp;compilation&nbsp;problems:&nbsp;<br />Void&nbsp;methods&nbsp;cannot&nbsp;return&nbsp;a&nbsp;value</p>
<p>&nbsp;</p>
<p><b>상황</b></p>
<p>첨부파일은 그대로 잘 들어갔는데 파일 업로드 실패라고 떴다</p>
<p><figure class="imageblock alignCenter"><span><img height="684" src="https://blog.kakaocdn.net/dn/dojeYz/btroOD2RLXp/LzahXfMTwk7JiqGqVdseX1/img.png" width="1218" /></span></figure>
</p>
<h2><span style="color: #ee2323;"><b>원인</b></span></h2>
<h2><span style="color: #ee2323;"><b>isUpload = true;</b></span></h2>
<p><span style="color: #ee2323;"><b>이게 빠져서 오류가 났다</b></span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>