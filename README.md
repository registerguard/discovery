# discovery
A [Tarbell-powered](http://http://www.tarbell.io/) print &amp; Web directory listings maker for [Discovery magazine](http://cloud.registerguard.com/discovery/), a interactive publication of RG Media Company, [registerguard.com](http://registerguard.com) and _The Register-Guard_, in Eugene, Ore.

### Note
To get the Jinja2 templating to work, in the Google Sheet it's likely you'll have to grep `\r|\n|\r\n` out all the carriage returns that people like to enter into spreadsheet cells.  

For the mapping lat & lngs, verify that the `lat_live` & `lng_live` rows/columns are valid. (Where there's chit-chat mixed in with the address, the clean address has been copied into a green row. e.g., breweries ... ) JavaScript/Leaflet use the static `0lat` & `lng` columns. In the case of changes/updates, you may need to copy the live values into the static `lat` & `lng` columns.

If you get:
```bash
Using default bucket credentials

Error: S3 error! See below:

S3ResponseError: 301 Moved Permanently
```
You may also may need to change the `host` setting in the `[s3]` section of your `~/.boto` settings file to the region you're trying to push to.