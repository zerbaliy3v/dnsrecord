
Discourse.Markdown.whiteListTag(‘script’, ‘type’, ‘text/javascript’);
Discourse.Markdown.whiteListTag(‘script’, ‘src’, /https://asciinema.org/a/\d+.js/);
Discourse.Markdown.whiteListTag(‘script’, ‘id’, ‘*’);
Discourse.Markdown.whiteListTag(‘script’, ‘async’);
