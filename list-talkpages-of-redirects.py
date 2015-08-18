#! /usr/bin/env python3

from ws.core import API

def main(api):
    # get titles of all redirect pages in 'Main', 'ArchWiki' and 'Help' namespaces
    redirect_titles = []
    for ns in ["0", "4", "12"]:
        _pages = api.generator(generator="allpages", gaplimit="max", gapfilterredir="redirects", gapnamespace=ns)
        redirect_titles.extend([page["title"] for page in _pages])

    # get titles of all pages in 'Talk', 'ArchWiki talk' and 'Help talk' namespaces
    talks = []
    for ns in ["1", "5", "13"]:
        # limiting to talk pages that are not redirects is also useful
    #    pages = api.generator(generator="allpages", gaplimit="max", gapnamespace=ns)
        pages = api.generator(generator="allpages", gaplimit="max", gapfilterredir="nonredirects", gapnamespace=ns)
        talks.extend([page["title"] for page in pages])

    # print talk pages associated to a redirect page
    for title in sorted(redirect_titles):
        namespace, pure_title = api.detect_namespace(title)
        talk_prefix = namespace + " talk:" if namespace != "" else "Talk:"
        talk = talk_prefix + pure_title
        if talk in talks:
            print("* [[%s]]" % talk)

if __name__ == "__main__":
    import ws.config
    api = ws.config.object_from_argparser(API, description="List talk pages of redirects")
    main(api)
