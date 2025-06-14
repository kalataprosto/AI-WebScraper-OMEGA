from mitmproxy import http

class ScrapeProxy:
    def request(self, flow: http.HTTPFlow):
        if "api" in flow.request.url:
            flow.request.headers["X-Proxy-Injected"] = "true"

    def response(self, flow: http.HTTPFlow):
        if "json" in flow.response.headers.get("content-type", ""):
            flow.response.text = flow.response.text.replace(
                '"data":', '"data": [HACKED BY SCRAPEMASTER]'
            )
