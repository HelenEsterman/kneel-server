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

    def do_DELETE(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            if view.__module__ == "views.OrderView":
                view.delete(self, url["pk"])
            else:
                view.delete_put_post(self)
        except AttributeError:
            return self.response(
                "No view for that route",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )

    def do_PUT(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            if view.__module__ == "views.OrderView":
                view.put(self)
            else:
                view.delete_put_post(self)
        except AttributeError:
            return self.response(
                "No view for that route",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )

    def do_POST(self):
        # Parse the URL
        url = self.parse_url(self.path)
        # Determine the correct view needed to handle the requests
        view = self.determine_view(url)
        # Get the request body
        request_body = self.get_request_body()
        # Invoke the correct method on the view
        try:
            if view.__module__ == "views.OrderView":
                view.post(self, request_body)
            else:
                view.delete_put_post(self)
        # Make sure you handle the AttributeError in case the client requested a route that you don't support
        except AttributeError:
            return self.response(
                "Unable to post", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
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
