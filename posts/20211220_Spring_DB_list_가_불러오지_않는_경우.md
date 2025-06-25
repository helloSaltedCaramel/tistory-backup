# Spring DB list 가 불러오지 않는 경우

*발행: Mon, 20 Dec 2021 13:12:09 +0900*

---

<p style="text-align: left;"><span style="background-color: #dddddd;"><b>error 화면&nbsp;</b></span></p>
<p style="text-align: left;"><span style="background-color: #dddddd;"><b>DB 안에 컬럼 리스트가 들어있는데 출력이 되지 않음.&nbsp;</b></span></p>
<p>&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="798" src="https://blog.kakaocdn.net/dn/nNmGD/btrolT4HRni/2s4uQvfboQw3h4Qs6fs361/img.png" width="1820" /></span></figure>
</p>
<p><span style="background-color: #dddddd;">원인</span></p>
<p><span style="background-color: #dddddd;">jsp 페이지에서 tablib를 써주지 않아서 리스트를 불러오지 못함</span></p>
<p><figure class="imageblock alignCenter"><span><img height="512" src="https://blog.kakaocdn.net/dn/Bu8CC/btrogv4RHgm/e0IHHztNa2c2ldHO4lKZxK/img.png" width="1272" /></span></figure>
</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>해결방안</p>
<p><span>&lt;%@</span><span> </span><span><b>taglib</b></span><span> </span><span>prefix</span><span>=</span><i>"c"</i><span> </span><span>uri</span><span>=</span><i>"<a href="http://java.sun.com/jsp/jstl/core">http://java.sun.com/jsp/jstl/core</a>"</i><span> </span><span>%&gt;</span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h2 style="text-align: center;"><b>taglib의 역할</b></h2>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>[참고사이트]</p>
<p><a href="https://atoz-develop.tistory.com/entry/JSP-JSTL-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-%EC%A3%BC%EC%9A%94-%ED%83%9C%EA%B7%B8-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC" rel="noopener" target="_blank">https://atoz-develop.tistory.com/entry/JSP-JSTL-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-%EC%A3%BC%EC%9A%94-%ED%83%9C%EA%B7%B8-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC</a></p>
<figure contenteditable="false" id="og_1639970964021"><a href="https://atoz-develop.tistory.com/entry/JSP-JSTL-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-%EC%A3%BC%EC%9A%94-%ED%83%9C%EA%B7%B8-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC" rel="noopener" target="_blank">
<div class="og-image">&nbsp;</div>
<div class="og-text">
<p class="og-title">[JSP] JSTL 사용 방법 - 주요 태그 문법 정리</p>
<p class="og-desc">JSTL을 사용하려면 라이브러리가 필요하다. 라이브러리 다운로드 및 프로젝트 세팅은 이 포스트를 참고한다. 태그 라이브러리 선언 자바에서 import문을 선언하듯 JSP에서도 JSTL 확장 태그를 사용</p>
<p class="og-host">atoz-develop.tistory.com</p>
</div>
</a></figure>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>태그 라이브러리 선언</p>
<p>: 자바에서 import문을 선언하듯 JSP에서도 JSTL확장 태그를 사용하려면 taglib 지시자로 라이브러리를 선언 해야한다. JSP 지시자 태그&lt;%@taglib%&gt;를 사용해서 다음과 같이 선언한다.</p>
<p>&nbsp;</p>
<blockquote>&lt;%@ taglib prefix="접두사" uri="URI" %&gt;</blockquote>
<p>&nbsp;</p>
<p>uri : 태그 라이브러리의 네임 스페이스 URI 식별자</p>
<p>prefix : JSTL 태그를 사용할때 태그 이름 앞에 붙일 접두사</p>
<p>&nbsp;</p>
<p>다음은 태그 라이브러리 별 표준 선언문이다.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>