from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import MetalView, StyleView, SizeView, OrderView


class JSONServer(HandleRequests):
    def do_GET(self):
        # dividing url up into dictionary to use
        url = self.parse_url(self.path)
        # based on certain properties of the url the determine_view function runs and checks
        # which view is needed (view will correspond with "requested_resource" on URL)
        view = self.determine_view(url)

        try:
            view.get(self, url["pk"])
        except AttributeError:
            return self.response(
                "No view for that route",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )

    def determine_view(self, url):
        """Lookup the correct view class to handle the requested route

        Args:
            url (dict): The URL dictionary

        Returns:
            Any: An instance of the matching view class
        """
        try:
            routes = {
                "metals": MetalView,
                "sizes": SizeView,
                "styles": StyleView,
                "orders": OrderView,
            }

            matching_class = routes[url["requested_resource"]]
            return matching_class()
        except KeyError:
            return status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value


# this makes JSON run properly :)
def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
