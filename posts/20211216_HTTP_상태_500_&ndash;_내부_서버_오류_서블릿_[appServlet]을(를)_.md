# HTTP 상태 500 &ndash; 내부 서버 오류/ 서블릿 [appServlet]을(를) 위한 Servlet.init() 호출이 예외를 발생시켰습니다.

*발행: Thu, 16 Dec 2021 16:11:26 +0900*

---

<h3><span style="color: #006dd7;"><b>Error 메세지</b></span></h3>
<p><figure class="imageblock alignCenter"><span><img height="942" src="https://blog.kakaocdn.net/dn/VUwc3/btrn6PViAcX/j8Xh6FkOYm8JKSjbYz8FEK/img.png" width="3228" /></span></figure>
</p>
<h1>&nbsp;</h1>
<h1><span style="color: #006dd7;">HTTP 상태 500 &ndash; 내부 서버 오류</span></h1>
<hr class="line" />
<p><b>타입</b><span>&nbsp;</span>예외 보고</p>
<p><b>메시지</b><span>&nbsp;</span>서블릿 [appServlet]을(를) 위한 Servlet.init() 호출이 예외를 발생시켰습니다.</p>
<p><b>설명</b><span>&nbsp;</span>서버가, 해당 요청을 충족시키지 못하게 하는 예기치 않은 조건을 맞닥뜨렸습니다.</p>
<p><b>예외</b></p>
<pre class="stylus"><code>javax.servlet.ServletException: 서블릿 [appServlet]을(를) 위한 Servlet.init() 호출이 예외를 발생시켰습니다.
	org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:540)
	org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
	org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
	org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:357)
	org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:382)
	org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
	org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:895)
	org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1732)
	org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
	org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
	org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
	org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
	java.base/java.lang.Thread.run(Thread.java:834)
</code></pre>
<p><b>근본 원인 (root cause)</b></p>
<pre class="routeros"><code>org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'memberController': Injection of autowired dependencies failed; nested exception is org.springframework.beans.factory.BeanCreationException: Could not autowire field: private com.sist.model.MemberDAO com.sist.jdbc03.MemberController.dao; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No matching bean of type [com.sist.model.MemberDAO] found for dependency: expected at least 1 bean which qualifies as autowire candidate for this dependency. Dependency annotations: {@org.springframework.beans.factory.annotation.Autowired(required=true)}</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="color: #ee2323;">해결방법&nbsp;</span></p>
<p>@Repository 가 빠져서 난 오류이다.&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="450" src="https://blog.kakaocdn.net/dn/bv19Jv/btrn14THm7V/Zt3HlKZNnXqUNvAYaZKJK0/img.png" width="1008" /></span></figure>
</p>
<p>&nbsp;</p>