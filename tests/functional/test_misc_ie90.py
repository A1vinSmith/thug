import os
import logging

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestMiscSamplesIE(object):
    cwd_path  = os.path.dirname(os.path.realpath(__file__))
    misc_path = os.path.join(cwd_path, os.pardir, "samples/misc")

    def do_perform_test(self, caplog, sample, expected, nofetch = False):
        xmlhttp = getattr(log, 'XMLHTTP', None)
        if xmlhttp:
            delattr(log, 'XMLHTTP')

        thug = ThugAPI()

        thug.set_useragent('win7ie90')
        thug.set_events('click,storage')
        thug.set_connect_timeout(2)
        thug.disable_cert_logging()
        thug.set_ssl_verify()
        thug.set_features_logging()

        if nofetch:
            thug.set_no_fetch()

        thug.log_init(sample)
        thug.run_local(sample)

        records = [r.message for r in caplog.records]

        matches = 0

        for e in expected:
            for record in records:
                if e in record:
                    matches += 1

        assert matches >= len(expected)

    def test_plugindetect1(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.6.html")
        expected = ['AdobeReader version: 9.1.0.0',
                    'Flash version: 10.0.64.0']

        self.do_perform_test(caplog, sample, expected)

    def test_plugindetect2(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.8.html")
        expected = ['AdobeReader version: 9,1,0,0',
                    'Flash version: 10,0,64,0',
                    'Java version: 1,6,0,32',
                    'ActiveXObject: javawebstart.isinstalled.1.6.0.0',
                    'ActiveXObject: javaplugin.160_32']

        self.do_perform_test(caplog, sample, expected)

    def test_test1(self, caplog):
        sample   = os.path.join(self.misc_path, "test1.html")
        expected = ['[Window] Alert Text: one']
        self.do_perform_test(caplog, sample, expected)

    def test_test2(self, caplog):
        sample   = os.path.join(self.misc_path, "test2.html")
        expected = ['[Window] Alert Text: Java enabled: true']
        self.do_perform_test(caplog, sample, expected)

    def test_test3(self, caplog):
        sample   = os.path.join(self.misc_path, "test3.html")
        expected = ['[Window] Alert Text: foo']
        self.do_perform_test(caplog, sample, expected)

    def test_test4(self, caplog):
        sample   = os.path.join(self.misc_path, "test4.js")
        expected = ['[Window] Alert Text: Test']
        self.do_perform_test(caplog, sample, expected)

    def test_testAppendChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testAppendChild.html")
        expected = ['Don\'t care about me',
                    'Just a sample',
                    'Attempt to append a null element failed',
                    'Attempt to append an invalid element failed',
                    'Attempt to append a text element failed',
                    'Attempt to append a read-only element failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testClipboardData(self, caplog):
        sample   = os.path.join(self.misc_path, "testClipboardData.html")
        expected = ['Test ClipboardData']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode.html")
        expected = ['<div id="cloned"><q>Can you copy <em>everything</em> I say?</q></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode2.html")
        expected = ['[Window] Alert Text: [object HTMLButtonElement]',
                    '[Window] Alert Text: Clone node',
                    '[Window] Alert Text: None',
                    '[Window] Alert Text: [object Attr]',
                    '[Window] Alert Text: True']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateHTMLDocument(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateHTMLDocument.html")
        expected = ['[object HTMLDocument]',
                    '[object HTMLBodyElement]',
                    '<p>This is a new paragraph.</p>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateStyleSheet(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateStyleSheet.html")
        expected = ['[Window] Alert Text: style1.css',
                    '[Window] Alert Text: style2.css',
                    '[Window] Alert Text: style3.css',
                    '[Window] Alert Text: style4.css']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentAll(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentAll.html")
        expected = ["http://www.google.com"]
        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentWrite1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentWrite1.html")
        expected = ['Foobar',
                    "Google</a><script>alert('foobar');</script><script language=\"VBScript\">alert('Gnam');</script><script>alert('Aieeeeee');</script></body>"]
        self.do_perform_test(caplog, sample, expected)

    def test_testExternalSidebar(self, caplog):
        sample   = os.path.join(self.misc_path, "testExternalSidebar.html")
        expected = ['[Window] Alert Text: Internet Explorer >= 7.0 or Chrome']
        self.do_perform_test(caplog, sample, expected)

    def test_testGetElementsByClassName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByClassName.html")
        expected = ['First',
                    'Hello World!',
                    'Second']
        self.do_perform_test(caplog, sample, expected)

    def test_testInnerHTML(self, caplog):
        sample   = os.path.join(self.misc_path, "testInnerHTML.html")
        expected = ['dude', 'Fred Flinstone']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertBefore(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertBefore.html")
        expected = ["<div>Just a sample</div><div>I'm your reference!</div></body></html>",
                    "[ERROR] Attempting to insert null element",
                    "[ERROR] Attempting to insert an invalid element",
                    "[ERROR] Attempting to insert using an invalid reference element",
                    "[ERROR] Attempting to insert a text node using an invalid reference element"]

        self.do_perform_test(caplog, sample, expected)

    def test_testLocalStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocalStorage.html")
        expected = ["Alert Text: Fired",
                    "Alert Text: bar",
                    "Alert Text: south"]
        self.do_perform_test(caplog, sample, expected)

    def test_testPlugins(self, caplog):
        sample   = os.path.join(self.misc_path, "testPlugins.html")
        expected = ["Shockwave Flash 10.0.64.0",
                    "Windows Media Player 7",
                    "Adobe Acrobat"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation1(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation1.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation1_nofetch(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation1.html")
        expected = ["Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected, nofetch = True)

    def test_testLocation2(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation2.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation3(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation3.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation4(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation4.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation5(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation5.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation6(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation6.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation7(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation7.html")
        expected = ["[window open redirection] about:blank -> https://buffer.antifork.org"]

        self.do_perform_test(caplog, sample, expected)

    def test_testLocation8(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation8.html")
        expected = ["[window open redirection] about:blank -> https://buffer.antifork.org"]

        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEdge(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEdge.html")
        expected = ["[Window] Alert Text: 9"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEmulateIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEmulateIE.html")
        expected = ["[Window] Alert Text: 8"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleIE.html")
        expected = ["[Window] Alert Text: 9"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode.html")
        expected = ["thelink",
                    "thediv"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode2.html")
        expected = ["thelink",
                    "thediv2"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector.html")
        expected = ["Alert Text: Have a Good life.",
                    "CoursesWeb.net"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector2(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector2.html")
        expected = ['CoursesWeb.net',
                    "MarPlo.net",
                    'php.net']
        self.do_perform_test(caplog, sample, expected)

    def test_testScope(self, caplog):
        sample   = os.path.join(self.misc_path, "testScope.html")
        expected = ["foobar",
                    "foo",
                    "bar",
                    "True",
                    "3",
                    "2012-10-07 11:13:00",
                    "3.14159265359",
                    "/foo/i"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSessionStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testSessionStorage.html")
        expected = ["key1",
                    "key2",
                    "value1",
                    "value3"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSetInterval(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetInterval.html")
        expected = ["[Window] Alert Text: Hello"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSetInterval2(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetInterval2.html")
        expected = ["[Window] Alert Text: Hello"]
        self.do_perform_test(caplog, sample, expected)

    def test_testText(self, caplog):
        sample   = os.path.join(self.misc_path, "testText.html")
        expected = ['<p id="p1">First line of paragraph.<br/> Some text added dynamically. </p>']
        self.do_perform_test(caplog, sample, expected)

    def test_testWindowOnload(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindowOnload.html")
        expected = ["[Window] Alert Text: Fired"]
        self.do_perform_test(caplog, sample, expected)

    def test_test_click(self, caplog):
        sample   = os.path.join(self.misc_path, "test_click.html")
        expected = ["[window open redirection] about:blank -> https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML1(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML1.html")
        expected = ['<div id="five">five</div><div id="one">one</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML2(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML2.html")
        expected = ['<div id="two"><div id="six">six</div>two</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML3(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML3.html")
        expected = ['<div id="three">three<div id="seven">seven</div></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML4(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML4.html")
        expected = ['<div id="four">four</div><div id="eight">eight</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML5(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML5.html")
        expected = ['insertAdjacentHTML does not support notcorrect operation']
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent1(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent1.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent2(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent2.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent3(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent3.html")
        expected = ["LoadLibraryA",
                    "URLDownloadToFile",
                    "http://www.360.cn.sxxsnp2.cn/d5.css",
                    "WinExec",
                    "U.exe",
                    "ExitProcess"]

        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent4(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent4.html")
        expected = ["[Microsoft XMLHTTP ActiveX] open('POST', 'http://192.168.1.100', True, 'foo', 'bar')",
                    "[Microsoft XMLHTTP ActiveX] send('TEST')"]

        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent5(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent5.html")
        expected = ["[Window] Alert Text: Request completed",
                    "[JNLP Detected]"]

        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent6(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent6.html")
        expected = ["[Window] Alert Text: Request completed",
                    "[JSON redirection]"]

        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent7(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent7.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent8(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent8.html")
        expected = ['window: [object Window]',
                    'self: [object Window]',
                    'top: [object Window]',
                    'length: 0',
                    'history: [object History]',
                    'pageXOffset: 0',
                    'pageYOffset: 0',
                    'screen: [object Screen]',
                    'screenLeft: 0',
                    'screenX: 0',
                    'confirm: true']

    def test_testMicrosoftXMLHTTPEvent9(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent9.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testCurrentScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testCurrentScript.html")
        expected = ["[Window] Alert Text: This page has scripts",
                    "[Window] Alert Text: text/javascript",
                    "[Window] Alert Text: Just a useless script"]
        self.do_perform_test(caplog, sample, expected)

    def test_testFormSubmit(self, caplog):
        sample   = os.path.join(self.misc_path, "testFormSubmit.html")
        expected = ["[form redirection] about:blank -> https://www.bing.com"]
        self.do_perform_test(caplog, sample, expected)

    def test_testCCInterpreter(self, caplog):
        sample   = os.path.join(self.misc_path, "testCCInterpreter.html")
        expected = ['JavaScript version: 9',
                    'Running on the 32-bit version of Windows']
        self.do_perform_test(caplog, sample, expected)

    def test_testTextNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextNode.html")
        expected = ['nodeName: #text',
                    'nodeType: 3',
                    'Object: [object Text]',
                    'nodeValue: Hello World',
                    'Length: 11',
                    'Substring(2,5): llo W',
                    'New nodeValue (replace): HelloAWorld',
                    'New nodeValue (delete 1): HelloWorld',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): Hello',
                    'New nodeValue (append): Hello Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): Hello New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testCommentNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCommentNode.html")
        expected = ['nodeName: #comment',
                    'nodeType: 8',
                    'Object: [object Comment]',
                    'nodeValue: <!--Hello World-->',
                    'Length: 18',
                    'Substring(2,5): --Hel',
                    'New nodeValue (replace): <!--HAllo World-->',
                    'New nodeValue (delete 1): <!--Hllo World-->',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): <!--H',
                    'New nodeValue (append): <!--H Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): <!--H New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testDOMImplementation(self, caplog):
        sample   = os.path.join(self.misc_path, "testDOMImplementation.html")
        expected = ["hasFeature('core'): true", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testAttrNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testAttrNode.html")
        expected = ['Object: [object Attr]',
                    'nodeName: test',
                    'nodeType: 2',
                    'nodeValue: foo',
                    'Length: undefined',
                    'New nodeValue: test2',
                    'Parent: null',
                    'Owner: null',
                    'Name: test',
                    'Specified: true',
                    'childNodes length: 0']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild.html")
        expected = ['firstChild: Old child',
                    'lastChild: Old child',
                    'innerText: Old child',
                    '[ERROR] Attempting to replace with a null element',
                    '[ERROR] Attempting to replace a null element',
                    '[ERROR] Attempting to replace with an invalid element',
                    '[ERROR] Attempting to replace an invalid element',
                    '[ERROR] Attempting to replace on a read-only element failed',
                    'Alert Text: New child',
                    '<div id="foobar"><!--Just a comment--></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCookie(self, caplog):
        sample   = os.path.join(self.misc_path, "testCookie.html")
        expected = ['favorite_food=tripe',
                    'name=oeschger' ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment1.html")
        expected = ["<div><p>Test</p></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment2(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment2.html")
        expected = ["<div id=\"foobar\"><b>This is B</b></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment3(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment3.html")
        expected = ["foo:bar", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment4(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment4.html")
        expected = ['<div><p>Test2</p></div><div><p>Test</p></div><div id="test1"><p>Test 1</p></div>', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment5(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment5.html")
        expected = ['Trying to replace a node not in the tree',
                    '<div><p>Test2</p></div><div><p>Test</p></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentType(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentType.html")
        expected = ['Doctype: [object DocumentType]',
                    'Doctype name: html',
                    'Doctype nodeName: html',
                    'Doctype nodeType: 10',
                    'Doctype nodeValue: null',
                    'Doctype publicId: ',
                    'Doctype systemId: ',
                    'Doctype textContent: null']

        self.do_perform_test(caplog, sample, expected)

    def test_testRemoveChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testRemoveChild.html")
        expected = ['<div>Don\'t care about me</div>',
                    '[ERROR] Attempting to remove null element',
                    '[ERROR] Attempting to remove an invalid element',
                    '[ERROR] Attempting to remove a read-only element',
                    '[ERROR] Attempting to remove an element not in the tree',
                    '[ERROR] Attempting to remove from a read-only element']

        self.do_perform_test(caplog, sample, expected)

    def test_testNamedNodeMap(self, caplog):
        sample   = os.path.join(self.misc_path, "testNamedNodeMap.html")
        expected = ['hasAttributes (before removal): true',
                    'hasAttribute(\'id\'): true',
                    'First test: id->p1',
                    'Second test: id->p1',
                    'Third test: id->p1',
                    'Fourth test: id->p1',
                    'Fifth test failed',
                    'Not existing: null',
                    'hasAttributes (after removal): false',
                    'Sixth test: foo->bar',
                    'Seventh test: foo->bar2',
                    'Final attributes length: 1']

        self.do_perform_test(caplog, sample, expected)

    def test_testEntityReference(self, caplog):
        sample   = os.path.join(self.misc_path, "testEntityReference.html")
        expected = ['node: [object EntityReference]',
                    'name: &',
                    'nodeName: &',
                    'nodeType: 5',
                    'nodeValue: null']

        self.do_perform_test(caplog, sample, expected)

    def test_getElementsByTagName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByTagName.html")
        expected = ['[object HTMLHtmlElement]',
                    '[object HTMLHeadElement]',
                    '[object HTMLBodyElement]',
                    '[object HTMLParagraphElement]',
                    '[object HTMLScriptElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentElement.html")
        expected = ['<a href="http://www.google.com">Google</a>']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute1(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute1.html")
        expected = ['Attribute: bar',
                    'Attribute (after removal): null']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute2(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute2.html")
        expected = ['[element workaround redirection] about:blank -> https://buffer.github.io/thug/notexists.html',
                    '[element workaround redirection] about:blank -> https://buffer.github.io/thug/']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute3(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute3.html")
        expected = ['Alert Text: foo',
                    'Alert Text: bar',
                    'Alert Text: test',
                    'Alert Text: foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testCDATASection(self, caplog):
        sample   = os.path.join(self.misc_path, "testCDATASection.html")
        expected = ['nodeName: #cdata-section',
                    'nodeType: 4',
                    '<xml>&lt;![CDATA[Some &lt;CDATA&gt; data &amp; then some]]&gt;</xml>']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLCollection.html")
        expected = ['<div id="odiv1">Page one</div>',
                    '<div name="odiv2">Page two</div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testDOMImplementation2(self, caplog):
        sample   = os.path.join(self.misc_path, "testDOMImplementation2.html")
        expected = ['Element #1: [object HTMLHeadElement]',
                    'Element #2: [object HTMLLinkElement]',
                    'Element #3: [object HTMLTitleElement]',
                    'Element #4: [object HTMLMetaElement]',
                    'Element #5: [object HTMLBaseElement]',
                    'Element #6: [object HTMLIsIndexElement]',
                    'Element #7: [object HTMLStyleElement]',
                    'Element #8: [object HTMLFormElement]',
                    'Element #9: [object HTMLSelectElement]',
                    'Element #10: [object HTMLOptGroupElement]',
                    'Element #11: [object HTMLOptionElement]',
                    'Element #12: [object HTMLInputElement]',
                    'Element #13: [object HTMLTextAreaElement]',
                    'Element #14: [object HTMLButtonElement]',
                    'Element #15: [object HTMLLabelElement]',
                    'Element #16: [object HTMLFieldSetElement]',
                    'Element #17: [object HTMLLegendElement]',
                    'Element #18: [object HTMLUListElement]',
                    'Element #19: [object HTMLOListElement]',
                    'Element #20: [object HTMLDListElement]',
                    'Element #21: [object HTMLDirectoryElement]',
                    'Element #22: [object HTMLMenuElement]',
                    'Element #23: [object HTMLLIElement]',
                    'Element #24: [object HTMLDivElement]',
                    'Element #25: [object HTMLParagraphElement]',
                    'Element #26: [object HTMLHeadingElement]',
                    'Element #27: [object HTMLHeadingElement]',
                    'Element #28: [object HTMLHeadingElement]',
                    'Element #29: [object HTMLHeadingElement]',
                    'Element #30: [object HTMLHeadingElement]',
                    'Element #31: [object HTMLHeadingElement]',
                    'Element #32: [object HTMLQuoteElement]',
                    'Element #33: [object HTMLQuoteElement]',
                    'Element #34: [object HTMLSpanElement]',
                    'Element #35: [object HTMLPreElement]',
                    'Element #36: [object HTMLBRElement]',
                    'Element #37: [object HTMLBaseFontElement]',
                    'Element #38: [object HTMLFontElement]',
                    'Element #39: [object HTMLHRElement]',
                    'Element #40: [object HTMLModElement]',
                    'Element #41: [object HTMLModElement]',
                    'Element #42: [object HTMLAnchorElement]',
                    'Element #43: [object HTMLObjectElement]',
                    'Element #44: [object HTMLParamElement]',
                    'Element #45: [object HTMLImageElement]',
                    'Element #46: [object HTMLAppletElement]',
                    'Element #47: [object HTMLScriptElement]',
                    'Element #48: [object HTMLFrameSetElement]',
                    'Element #49: [object HTMLFrameElement]',
                    'Element #50: [object HTMLIFrameElement]',
                    'Element #51: [object HTMLTableElement]',
                    'Element #52: [object HTMLTableCaptionElement]',
                    'Element #53: [object HTMLTableColElement]',
                    'Element #54: [object HTMLTableColElement]',
                    'Element #55: [object HTMLTableSectionElement]',
                    'Element #56: [object HTMLTableSectionElement]',
                    'Element #57: [object HTMLTableSectionElement]',
                    'Element #58: [object HTMLTableRowElement]',
                    'Element #59: [object HTMLTableCellElement]',
                    'Element #60: [object HTMLTableCellElement]',
                    'Element #61: [object HTMLMediaElement]',
                    'Element #62: [object HTMLAudioElement]',
                    'Element #63: [object HTMLHtmlElement]',
                    'Element #64: [object HTMLBodyElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testApplyElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testApplyElement.html")
        expected = ['<div id="outer"><div id="test"><div>Just a sample</div></div></div>',
                    '<div id="outer"><div>Just a div<div id="test"><div>Just a sample</div></div></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testProcessingInstruction(self, caplog):
        sample   = os.path.join(self.misc_path, "testProcessingInstruction.html")
        expected = ['[object ProcessingInstruction]',
                    'nodeName: xml-stylesheet',
                    'nodeType: 7',
                    'nodeValue: href="mycss.css" type="text/css"',
                    'target: xml-stylesheet']

        self.do_perform_test(caplog, sample, expected)

    def test_testWindow(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindow.html")
        expected = ['window: [object Window]',
                    'self: [object Window]',
                    'top: [object Window]',
                    'length: 0',
                    'history: [object History]',
                    'pageXOffset: 0',
                    'pageYOffset: 0',
                    'screen: [object Screen]',
                    'screenLeft: 0',
                    'screenX: 0',
                    'confirm: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject1(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject1.html")
        expected = ['[object data redirection] about:blank -> https://github.com/buffer/thug/raw/master/tests/test_files/sample.swf']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject2(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject2.html")
        expected = ['[params redirection] about:blank -> http://192.168.1.100/data',
                    '[params redirection] about:blank -> http://192.168.1.100/source',
                    '[params redirection] about:blank -> http://192.168.1.100/archive']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject3(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject3.html")
        expected = ['[params redirection] about:blank -> http://192.168.1.100/movie.swf']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject4(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject4.html")
        expected = ['[params redirection] about:blank -> http://192.168.1.100/archive']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject5(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject5.html")
        expected = ['[params redirection] about:blank -> http://192.168.1.100/data',
                    '[params redirection] about:blank -> http://192.168.1.100/source',
                    '[params redirection] about:blank -> http://192.168.1.100/archive']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject7(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject7.html")
        expected = ['width: 400',
                    'foo: undefined',
                    'foo: bar']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild2(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild2.html")
        expected = ['<div id="foobar"><div id="test"></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testNavigator(self, caplog):
        sample   = os.path.join(self.misc_path, "testNavigator.html")
        expected = ['window: [object Window]',
                    'appCodeName: Mozilla',
                    'appName: Microsoft Internet Explorer',
                    'appVersion: 5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; rv:9.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.2; BOIE9;ENUS)',
                    'cookieEnabled: true',
                    'onLine: true',
                    'platform: Win32']

        self.do_perform_test(caplog, sample, expected)

    def test_testWScriptShell(self, caplog):
        sample   = os.path.join(self.misc_path, "testWScriptShell.html")
        expected = ['ActiveXObject: wscript.shell',
                    'valueOf: Windows Script Host',
                    'toString: Windows Script Host',
                    '[WScript.Shell ActiveX] Sleep(1)',
                    '[WScript.Shell ActiveX] Environment("System")',
                    '[WScript.Shell ActiveX] Expanding environment string "Windows is installed in %WinDir%"',
                    '[WScript.Shell ActiveX] Expanded environment string to "Windows is installed in C:\\Windows"',
                    '[WScript.Shell ActiveX] Expanding environment string "Username: %USERNAME%"',
                    '[WScript.Shell ActiveX] Expanding environment string "Computer name: %COMPUTERNAME%"',
                    '[WScript.Shell ActiveX] Expanding environment string "OS: %OS%"',
                    '[WScript.Shell ActiveX] Expanded environment string to "OS: WINDOWS_NT"',
                    '[WScript.Shell ActiveX] Expanding environment string "CommonProgramFiles: %CommonProgramFiles%"',
                    '[WScript.Shell ActiveX] Expanded environment string to "CommonProgramFiles: C:\\Program Files\\Common Files"',
                    '[WScript.Shell ActiveX] Echo(Echo test)',
                    '[WScript.Shell ActiveX] Received call to SpecialFolders property "AllUsersDesktop"',
                    '[WScript.Shell ActiveX] Expanding environment string "%PUBLIC%\\Desktop"',
                    '[WScript.Shell ActiveX] Expanded environment string to "C:\\Users\\Public\\Desktop"',
                    '[WScript.Shell ActiveX] Received call to SpecialFolders property "AllUsersStartMenu"',
                    '[WScript.Shell ActiveX] Expanding environment string "%ALLUSERSPROFILE%\\Microsoft\\Windows\\Start Menu"',
                    '[WScript.Shell ActiveX] Expanded environment string to "C:\\ProgramData\\Microsoft\\Windows\\Start Menu"',
                    '[WScript.Shell ActiveX] RegRead("HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Systemroot") = "C:\\Windows"',
                    '[WScript.Shell ActiveX] RegWrite("HKCU\\MyNewKey\\", "1", "REG_DWORD")',
                    '[WScript.Shell ActiveX] RegRead("HKCU\\MyNewKey\\") = "1"',
                    '[WScript.Shell ActiveX] RegRead("HKLM\\Not Existing\\") = NOT FOUND',
                    '[WScript.Shell ActiveX] RegRead("HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\ProgramFilesDir") = "C:\\Program Files"',
                    '[WScript.Shell ActiveX] CreateShortcut "C:\\Program Files\\notepad.lnk"',
                    '[WScript.Shell ActiveX] CreateObject (wscript.shortcut)',
                    'ActiveXObject: wscript.shortcut',
                    '[WScript.Shortcut ActiveX] Saving link object \'C:\\Program Files\\notepad.lnk\' with target \'notepad.exe\'',
                    '[WScript.Shell ActiveX] Quit(1)']

        self.do_perform_test(caplog, sample, expected)

    def test_testAdodbStream(self, caplog):
        sample   = os.path.join(self.misc_path, "testAdodbStream.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Adodb.Stream)',
                    '[Window] Alert Text: Stream content: Test',
                    '[Window] Alert Text: Stream content (first 2 chars): Te',
                    '[Window] Alert Text: Stream size: 4',
                    '[Adodb.Stream ActiveX] SaveToFile(test.txt, 2)',
                    '[Adodb.Stream ActiveX] LoadFromFile(test1234.txt)',
                    '[Window] Alert Text: Attempting to load from a not existing file',
                    '[Adodb.Stream ActiveX] LoadFromFile(test.txt)',
                    '[Window] Alert Text: ReadText: Test',
                    '[Window] Alert Text: ReadText(3): Tes',
                    '[Window] Alert Text: ReadText(10): Test',
                    '[Adodb.Stream ActiveX] Changed position in fileobject to: (2)',
                    '[Window] Alert Text: stTest2',
                    '[Adodb.Stream ActiveX] Close']

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptingFileSystemObject(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptingFileSystemObject.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Scripting.FileSystemObject ActiveX] Returning C:\\WINDOWS for GetSpecialFolder("0")',
                    '[Scripting.FileSystemObject ActiveX] Returning C:\\WINDOWS\\system32 for GetSpecialFolder("1")',
                    '[WScript.Shell ActiveX] Expanding environment string "%TEMP%"',
                    '[Window] Alert Text: FolderExists(\'C:\\Windows\\System32\'): true',
                    '[Window] Alert Text: FileExists(\'\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\drivers\\etc\\hosts\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: GetExtensionName("C:\\Windows\\System32\\test.txt"): .txt',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: [After CopyFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): true',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): false',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test3.txt\'): true']

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptingEncoder(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptingEncoder.html")
        expected = ['[Scripting.Encoder ActiveX] EncodeScriptFile(".js", "alert("test");", 0, ""', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLOptionsCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLOptionsCollection.html")
        expected = ['length: 4',
                    'item(0): Volvo',
                    'namedItem(\'audi\'): Audi',
                    'namedItem(\'mercedes\').value: mercedes',
                    '[After remove] item(0): Saab',
                    '[After first add] length: 4',
                    '[After first add] item(3): foobar',
                    '[After second add] length: 5',
                    '[After second add] item(3): test1234',
                    'Not found error']

        self.do_perform_test(caplog, sample, expected)

    def test_testTextStream(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextStream.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Scripting.FileSystemObject ActiveX] CreateTextFile("test.txt", "False", "False")',
                    '[After first write] ReadAll: foobar',
                    '[After first write] Line: 1',
                    '[After first write] Column: 7',
                    '[After first write] AtEndOfLine: true',
                    '[After first write] AtEndOfStream: true',
                    '[After second write] Line: 2',
                    '[After second write] Column: 1',
                    '[After second write] AtEndOfLine: false',
                    '[After second write] AtEndOfStream: false',
                    '[After third write] Line: 5',
                    '[After third write] Column: 16',
                    '[After third write] AtEndOfLine: false',
                    '[After third write] AtEndOfStream: false',
                    '[After fourth write] Line: 6',
                    '[After fourth write] Column: 1',
                    '[After fourth write] AtEndOfLine: false',
                    '[After fourth write] AtEndOfStream: false',
                    '[After fourth write] First char: s',
                    '[After fourth write] Second char: o',
                    '[After fourth write] Third char: m',
                    '[After fourth write] Line: some other textnext line',
                    '[After skip] Read(5): ttest']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLAnchorElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLAnchorElement.html")
        expected = ['a.protocol: https:',
                    'a.host: www.example.com:1234',
                    'a.hostname: www.example.com',
                    'a.port: 1234',
                    'b.protocol: :',
                    'b.host: ',
                    'b.hostname: ',
                    'b.port: ',
                    'c.protocol: https:',
                    'c.host: www.example.com',
                    'c.hostname: www.example.com',
                    'c.port: ',
                    'e.pathname: /foo/index.html']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLTableElement3(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLTableElement3.html")
        expected = ['tHead: [object HTMLTableSectionElement]',
                    'tHead row 0 sectionRowIndex: 0',
                    'tFoot: [object HTMLTableSectionElement]',
                    'caption: [object HTMLTableCaptionElement]',
                    'Row 0 rowIndex = 0',
                    'Row 1 rowIndex = 1',
                    'row: [object HTMLTableRowElement]',
                    'tBodies: [object HTMLCollection]',
                    'cell: [object HTMLTableCellElement]',
                    'cell.innerHTML: New cell 1',
                    'row.deleteCell(10) failed',
                    'row.deleteCell(20) failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testTextArea(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextArea.html")
        expected = ['type: textarea',
                    'cols: 100',
                    'rows: 25']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLDocument(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLDocument.html")
        expected = ['document.title: Test',
                    'document.title: Foobar',
                    'anchors: [object HTMLCollection]',
                    'anchors length: 1',
                    'anchors[0].name: foobar',
                    'applets: [object HTMLCollection]',
                    'applets length: 2',
                    'applets[0].code: HelloWorld.class',
                    'links: [object HTMLCollection]',
                    'links length: 1',
                    'links[0].href: https://github.com/buffer/thug/',
                    'images: [object HTMLCollection]',
                    'images length: 1',
                    'images[0].href: test.jpg',
                    'disabled: false',
                    'head: [object HTMLHeadElement]',
                    'referrer: ',
                    'URL: about:blank',
                    'Alert Text: Hello, world']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLFormElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLFormElement.html")
        expected = ['[object HTMLFormElement]',
                    'f.elements: [object HTMLFormControlsCollection]',
                    'f.length: 4',
                    'f.name: [object HTMLFormControlsCollection]',
                    'f.acceptCharset: ',
                    'f.action: /cgi-bin/test',
                    'f.enctype: application/x-www-form-urlencoded',
                    'f.encoding: application/x-www-form-urlencoded',
                    'f.method: POST',
                    'f.target: ']

        self.do_perform_test(caplog, sample, expected)

    def test_testFile(self, caplog):
        sample   = os.path.join(self.misc_path, "testFile.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Scripting.FileSystemObject ActiveX] GetFile("D:\\ Program Files\\ Common Files\\test.txt")',
                    '[File ActiveX] Path = D:\\ Program Files\\ Common Files\\test.txt, Attributes = 32',
                    'Drive (test.txt): D:',
                    'ShortPath (test.txt): D:\\\\ Progr~1\\\\ Commo~1\\\\test.txt',
                    'ShortName (test.txt): test.txt',
                    'Attributes: 1',
                    '[Scripting.FileSystemObject ActiveX] GetFile("test2.txt")',
                    '[File ActiveX] Path = test2.txt, Attributes = 32',
                    'Drive (test2.txt): C:',
                    'ShortPath (test2.txt): test2.txt',
                    'ShortName (test2.txt): test2.txt',
                    'Copy(test3.txt, True)',
                    'Move(test4.txt)',
                    'Delete(False)',
                    'OpenAsTextStream(ForReading, 0)']

        self.do_perform_test(caplog, sample, expected)

    def test_testFolder(self, caplog):
        sample   = os.path.join(self.misc_path, "testFolder.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Scripting.FileSystemObject ActiveX] CreateFolder("D:\\Program Files\\Test")',
                    '[Folder ActiveX] Path = D:\\Program Files\\Test, Attributes = 16',
                    'Drive: D:',
                    'ShortPath: D:\\\\Progra~1\\\\Test',
                    'ShortName: Test',
                    'Copy(D:\\Program Files\\Test2, True)',
                    'Move(D:\\Program Files\\Test3)',
                    'Delete(False)']

        self.do_perform_test(caplog, sample, expected)

    def test_testWScriptNetwork(self, caplog):
        sample   = os.path.join(self.misc_path, "testWScriptNetwork.html")
        expected = ['[WScript.Network ActiveX] Got request to PrinterConnections',
                    '[WScript.Network ActiveX] Got request to EnumNetworkDrives',
                    '[WScript.Shell ActiveX] Expanding environment string "%USERDOMAIN%"',
                    '[WScript.Shell ActiveX] Expanding environment string "%USERNAME%"',
                    '[WScript.Shell ActiveX] Expanding environment string "%COMPUTERNAME%"']

        self.do_perform_test(caplog, sample, expected)

    def test_testApplet(self, caplog):
        sample   = os.path.join(self.misc_path, "testApplet.html")
        expected = ['[applet redirection]']

        self.do_perform_test(caplog, sample, expected)

    def test_testFrame(self, caplog):
        sample   = os.path.join(self.misc_path, "testFrame.html")
        expected = ['[frame redirection]',
                    'Alert Text: https://buffer.github.io/thug/',
                    'Alert Text: data:text/html,<script>alert(\'Hello world\');</script>']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLAudioElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLAudioElement.html")
        expected = ['[object HTMLAudioElement]',
                    'src: https://buffer.github.io/thug/',
                    'controller: null',
                    'crossOrigin: null',
                    'currentSrc: https://buffer.github.io/thug/',
                    'initialTime: 0',
                    'currentTime: 0',
                    'muted: false',
                    'defaultMuted: false',
                    'readyState: 4',
                    'srcObject: null',
                    'playbackRate: 1',
                    'defaultPlaybackRate: 1',
                    'disableRemotePlayback: false',
                    'duration: 0',
                    'ended: false',
                    'error: null',
                    'mediaKeys: null',
                    'networkState: 1',
                    'audioTracks length: 0',
                    'textTracks length: 0',
                    'sinkId:',
                    'buffered length: 0',
                    'paused: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testIFrame(self, caplog):
        sample   = os.path.join(self.misc_path, "testIFrame.html")
        expected = ['[iframe redirection]',
                    'width: 3',
                    'height: 4']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLImageElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLImageElement.html")
        expected = ['src (before changes): test.jpg',
                    'src (after first change): test2.jpg',
                    'onerror handler fired']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLImageElement2(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLImageElement2.html")
        expected = ['Alert Text: Inside onerror handler',
                    '[ERROR][_handle_onerror] ReferenceError: foobar is not defined']

        self.do_perform_test(caplog, sample, expected)

    def test_testTitle(self, caplog):
        sample   = os.path.join(self.misc_path, "testTitle.html")
        expected = ['New title: Foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLMetaElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLMetaElement.html")
        expected = ['utf-8', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testScreen(self, caplog):
        sample   = os.path.join(self.misc_path, "testScreen.html")
        expected = ['window: [object Window]',
                    'screen: [object Screen]',
                    'availHeight: 600',
                    'availWidth: 800',
                    'colorDepth: 32',
                    'width: 800',
                    'bufferDepth: 24']

        self.do_perform_test(caplog, sample, expected)

    def test_testAcroPDF(self, caplog):
        sample   = os.path.join(self.misc_path, "testAcroPDF.html")
        expected = ['$version: 9.1.0', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testCSSStyleDeclaration(self, caplog):
        sample   = os.path.join(self.misc_path, "testCSSStyleDeclaration.html")
        expected = ['style: [object CSSStyleDeclaration]',
                    'length: 1',
                    'cssText: color: blue;',
                    'color: blue',
                    'item(0): color',
                    'item(100):',
                    'getPropertyValue(\'color\'): blue',
                    'length (after removeProperty): 0',
                    'cssText: foo: bar;']

        self.do_perform_test(caplog, sample, expected)

    def test_testFormProperty(self, caplog):
        sample   = os.path.join(self.misc_path, "testFormProperty.html")
        expected = ['[object HTMLFormElement]',
                    'formA']

        self.do_perform_test(caplog, sample, expected)

    def test_testVBScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testVBScript.html")
        expected = ['[VBS embedded URL redirection]',
                    'http://192.168.1.100/putty.exe']

        self.do_perform_test(caplog, sample, expected)

    def test_testFontFaceRule1(self, caplog):
        sample   = os.path.join(self.misc_path, "testFontFaceRule1.html")
        expected = ['[font face redirection]',
                    'http://192.168.1.100/putty.exe']

        self.do_perform_test(caplog, sample, expected)

    def test_testFontFaceRule2(self, caplog):
        sample   = os.path.join(self.misc_path, "testFontFaceRule2.html")
        expected = ['[font face redirection]',
                    'https://mdn.mozillademos.org/files/2468/VeraSeBd.ttf']

        self.do_perform_test(caplog, sample, expected)

    def test_testSilverLight(self, caplog):
        sample   = os.path.join(self.misc_path, "testSilverLight.html")
        expected = ['[SilverLight] isVersionSupported(\'4.0\')',
                    'Version 4.0 supported: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testHistory(self, caplog):
        sample   = os.path.join(self.misc_path, "testHistory.html")
        expected = ['history: [object History]',
                    'window: [object Window]',
                    'navigationMode (before change): automatic',
                    'navigationMode (after change): fast']

        self.do_perform_test(caplog, sample, expected)

    def test_testMSXML2Document(self, caplog):
        sample   = os.path.join(self.misc_path, "testMSXML2Document.html")
        expected = ['[MSXML2.DOMDocument] Microsoft XML Core Services MSXML Uninitialized Memory Corruption',
                    'CVE-2012-1889']

        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLDOM(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLDOM.html")
        expected = ['[Microsoft XMLDOM ActiveX] Creating element TEST',
                    'bin.base64',
                    'foobar3: foobar3',
                    'bin.hex',
                    'foobar4: foobar4']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLDocumentCompatibleInfo(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLDocumentCompatibleInfo.html")
        expected = ['This document is in IE 8 mode',
                    'compatMode = CSS1Compat',
                    'document.compatible.length = 1',
                    'userAgent = IE',
                    'version = 8']

        self.do_perform_test(caplog, sample, expected)

    def test_testEmbed(self, caplog):
        sample   = os.path.join(self.misc_path, "testEmbed.html")
        expected = ['[embed redirection]', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testWinNTSystemInfo(self, caplog):
        sample   = os.path.join(self.misc_path, "testWinNTSystemInfo.html")
        expected = ['[WScript.Shell ActiveX] CreateObject (WinNTSystemInfo)',
                    '[WinNTSystemInfo ActiveX] Getting ComputerName',
                    '[WinNTSystemInfo ActiveX] Getting DomainName',
                    '[WinNTSystemInfo ActiveX] Getting PDC (Primary Domain Controller)',
                    '[WinNTSystemInfo ActiveX] Getting UserName']

        self.do_perform_test(caplog, sample, expected)

    def test_testDump(self, caplog):
        sample   = os.path.join(self.misc_path, "testDump.html")
        expected = ['[eval] Deobfuscated argument: eval',
                    '[document.write] Deobfuscated argument: FOOBAR']

        self.do_perform_test(caplog, sample, expected)

    def test_testTimers(self, caplog):
        sample   = os.path.join(self.misc_path, "testTimers.html")
        expected = ['setTimeout null expression',
                    'setInterval null expression']

        self.do_perform_test(caplog, sample, expected)

    def test_testPlayStateChange(self, caplog):
        sample   = os.path.join(self.misc_path, "testPlayStateChange.html")
        expected = ['Undefined state']

        self.do_perform_test(caplog, sample, expected)

    def test_testAtob(self, caplog):
        sample   = os.path.join(self.misc_path, "testAtob.html")
        expected = ['Encoded String: SGVsbG8gV29ybGQ=',
                    'Decoded String: b\'Hello World\'']

        self.do_perform_test(caplog, sample, expected)

    def test_testExternal(self, caplog):
        sample   = os.path.join(self.misc_path, "testExternal.html")
        expected = []

        self.do_perform_test(caplog, sample, expected)

    def test_testAdodbRecordset(self, caplog):
        sample   = os.path.join(self.misc_path, "testAdodbRecordset.html")
        expected = ['ActiveXObject: adodb.recordset']

        self.do_perform_test(caplog, sample, expected)

    def test_testPrototype(self, caplog):
        sample   = os.path.join(self.misc_path, "testPrototype.html")
        expected = ['window.constructor: function Window()',
                    'window.prototype.__proto__: [object Object]',
                    'window.prototype.constructor: function Window()',
                    'window.prototype.name: Window',
                    'window.toLocaleString(): [object Window]',
                    'Greetings from get_var1',
                    'Greetings from set_var2',
                    'o.anotherValue = 5',
                    'isPrototypeOf (test 1): true',
                    'isPrototypeOf (test 2): true']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLBodyElement1(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLBodyElement1.html")
        expected = ['It works']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLBodyElement2(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLBodyElement2.html")
        expected = []

        self.do_perform_test(caplog, sample, expected)

    def test_testAsync(self, caplog):
        sample   = os.path.join(self.misc_path, "testAsync.html")
        expected = ['async: true', 'defer: false']

        self.do_perform_test(caplog, sample, expected)

    def test_testDefer(self, caplog):
        sample   = os.path.join(self.misc_path, "testDefer.html")
        expected = ['async: false', 'defer: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptSrc(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptSrc.html")
        expected = ['Alert Text: #foo']

        self.do_perform_test(caplog, sample, expected)

    def test_testClearTimeout(self, caplog):
        sample   = os.path.join(self.misc_path, "testClearTimeout.html")
        expected = ['Alert Text: 1',
                    'Alert Text: 2']

        self.do_perform_test(caplog, sample, expected)

    def test_testExecScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testExecScript.html")
        expected = ['Alert Text: execScript']

        self.do_perform_test(caplog, sample, expected)

    def test_testDecodeURIComponent(self, caplog):
        sample   = os.path.join(self.misc_path, "testDecodeURIComponent.html")
        expected = ['Alert Text: ~!@#$%^&*()=+[]{}\\;:\'",/?']

        self.do_perform_test(caplog, sample, expected)

    def test_testGetComputedStyle(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetComputedStyle.html")
        expected = ['lightblue']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLSelectElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLSelectElement.html")
        expected = ['True']

        self.do_perform_test(caplog, sample, expected)

    def test_meta_refresh(self, caplog):
        sample   = os.path.join(self.misc_path, "meta_refresh.html")
        expected = ['[meta redirection] about:blank -> https://buffer.github.io/thug/']

        self.do_perform_test(caplog, sample, expected)

    def test_js_data_src(self, caplog):
        sample   = os.path.join(self.misc_path, "testJSDataSrc.html")
        expected = ['[Window] Alert Text: Hello world']

        self.do_perform_test(caplog, sample, expected)

    def test_iframe_srcdoc(self, caplog):
        sample   = os.path.join(self.misc_path, "testIFrameSrcdoc.html")
        expected = ['[Window] Alert Text: Hello World']

        self.do_perform_test(caplog, sample, expected)

    def test_jscript(self, caplog):
        sample   = os.path.join(self.misc_path, "testJScript.html")
        expected = ['Rule: IE=EmulateIE8',
                    'Rule: JScript.Compact',
                    'Rule: JScript.Encode']

        self.do_perform_test(caplog, sample, expected)

    def test_testExecCommand(self, caplog):
         sample   = os.path.join(self.misc_path, "testExecCommand.html")
         expected = []

         self.do_perform_test(caplog, sample, expected)

    def test_testGetElementById(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementById.html")
        expected = ['[object HTMLDivElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testDomain(self, caplog):
        sample   = os.path.join(self.misc_path, "testDomain.html")
        expected = ["document.domain = github.com"]

        self.do_perform_test(caplog, sample, expected)

    def test_testJScriptEncode(self, caplog):
        sample   = os.path.join(self.misc_path, "testJScriptEncode.html")
        expected = ["this code should bE kept secret!!!!", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testIEVisibility(self, caplog):
        sample   = os.path.join(self.misc_path, "testIEVisibility.html")
        expected = ["[Window] Alert Text: document.msHidden: false",
                    "[Window] Alert Text: document.msVisibilityState: visible"]

        self.do_perform_test(caplog, sample, expected)

    def test_testSplitText(self, caplog):
        sample   = os.path.join(self.misc_path, "testSplitText.html")
        expected = ["p.childNodes.length before splitText: 1",
                    "foobar value after splitText: foo",
                    "bar value: bar",
                    "p.childNodes.length after splitText: 2"]

        self.do_perform_test(caplog, sample, expected)

    def test_testNormalize(self, caplog):
        sample   = os.path.join(self.misc_path, "testNormalize.html")
        expected = ["[Before normalize] wrapper.childNodes.length: 6",
                    "[After normalize] wrapper.childNodes.length: 3",
                    "[After normalize] wrapper.childNodes[0].textContent: Part 1 Part 2 Part 3",
                    "[After normalize] wrapper.childNodes[2].textContent: Part 4 Part 5"]

        self.do_perform_test(caplog, sample, expected)

    def test_testClearAttributes(self, caplog):
        sample   = os.path.join(self.misc_path, "testClearAttributes.html")
        expected = ["id: myMarquee",
                    "style: border:2px solid blue",
                    "bgcolor: null"]

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptingDictionary(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptingDictionary.html")
        expected = ["[Scripting.Dictionary ActiveX] Add(\"0\", \"1\")",
                    "[Scripting.Dictionary ActiveX] Add(\"1\", \"2\")",
                    "[Window] Alert Text: Count before removal: 2",
                    "[Window] Alert Text: Key 0 exists before removal: true",
                    "[Window] Alert Text: Key 1000 exists before removal: false",
                    "[Scripting.Dictionary ActiveX] Remove(\"0\")",
                    "[Scripting.Dictionary ActiveX] Remove(\"1000\")",
                    "[Window] Alert Text: Count after removal: 1",
                    "[Window] Alert Text: Key 0 exists after removal: false",
                    "[Window] Alert Text: Key 1000 exists after removal: false",
                    "[Scripting.Dictionary ActiveX] RemoveAll()",
                    "[Window] Alert Text: Count after RemoveAll: 0"]

        self.do_perform_test(caplog, sample, expected)
