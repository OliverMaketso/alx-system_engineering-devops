Postmortem
Upon the release of the ALX System Engineering & DevOps project 0x19, approximately 00:07 Pacific Standard Time (PST), an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file defining a simple WordPress site.

Debugging Process
Oliver Maketso, a seasoned bug debugger, faced a perplexing issue upon opening a new project. The problem arose at approximately 7:20 PM PST, and he immediately set out to resolve it.
First, he examined the running processes using the ps aux command. Two Apache2 processes, one running as root and the other as www-data, were functioning as expected. Next, he investigated the sites-available folder within the /etc/apache2/ directory. This revealed that the web server was serving content located in the /var/www/html/ directory.
To gain deeper insights, Oliver employed the strace tool. In one terminal, he ran strace on the PID of the root Apache process. Simultaneously, he curled the server in another terminal. However, this initial attempt yielded no valuable information from strace. Undeterred, he repeated the process, this time focusing on the PID of the www-data process.
With lower expectations, Oliver was pleasantly surprised when strace revealed an error message: "-1 ENOENT (No such file or directory)". The error occurred while attempting to access the file /var/www/html/wp-includes/class-wp-locale.phpp.
Intrigued, Oliver meticulously examined the files within the /var/www/html/ directory, utilizing Vim's pattern matching capabilities to locate the erroneous .phpp file extension. He eventually discovered the culprit in the wp-settings.php file, specifically on line 137. The line, require_once( ABSPATH . WPINC . '/class-wp-locale.php' );, contained the incorrect file extension.
Swiftly, Oliver removed the trailing "p" from the file extension. After making this modification, he conducted another curl test on the server. To his relief, the server responded with a 200 status code, indicating successful execution.


Wrote a Puppet manifest to automate fixing of the error.

Summation
In short, a typo. Gotta love'em. In full, the WordPress app was encountering a critical error in wp-settings.php when tyring to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php.

Patch involved a simple fix on the typo, removing the trailing p.

Prevention
This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.

Test! Test  test. Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

Status monitoring. Enable some uptime-monitoring service such as UptimeRobot to alert instantly upon outage of the website.

Note that in response to this error, I wrote a Puppet manifest 0-strace_is_your_friend.pp to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php.

But of course, it will never occur again, because we're programmers, and we never make errors! 😉
