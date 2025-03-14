# RepoTransBench Token Analysis

This project analyzes the token counts of Python files across repositories from the RepoTransBench dataset. By assessing the number of tokens per file and per repository, we aim to understand the size of these codebases, and to highlight that most of the repositories in the dataset are smaller than typical real-world projects.

## Results

`total_tokens` is the sum of the tokens in all **Python** files in the repository.

|repo_name                               |total_tokens|
|----------------------------------------|------------|
|Yelp___ephemeral-port-reserve           |882         |
|mike-grant___haaska                     |1208        |
|IlyaKrotov___BitMEX-simple-trading-robot|1262        |
|hmleal___py-clui                        |1291        |
|dwyl___english-words                    |1319        |
|rdegges___brute                         |1355        |
|emulbreh___pyffx                        |1363        |
|susam___mintotp                         |1431        |
|lukaskubis___darkskylib                 |1579        |
|Alir3z4___python-short_url              |1706        |
|suminb___base62                         |1932        |
|kevinwuhoo___randomcolor-py             |2059        |
|fastly___Avalanche                      |2088        |
|gnebehay___parser                       |2259        |
|dbrgn___coverage-badge                  |2265        |
|sha256___python-var-dump                |2292        |
|jundymek___free-proxy                   |2404        |
|liamja___Prebake                        |2467        |
|pyhackertarget___hackertarget           |2510        |
|sublee___glicko2                        |2598        |
|dashea___requests-file                  |2616        |
|barbosa___clorox                        |2640        |
|necaris___cuid.py                       |2640        |
|mozilla___unicode-slugify               |2649        |
|lzakharov___csv2md                      |2655        |
|alanhamlett___readtime                  |2704        |
|saresend___KSUID                        |2715        |
|liviu-___ding                           |2731        |
|mobify___iterstuff                      |2842        |
|jieter___python-lora                    |2851        |
|simon-weber___gpsoauth                  |2859        |
|peterjc___flake8-black                  |2904        |
|neural-dialogue-metrics___Distinct-N    |2948        |
|edsu___microdata                        |3013        |
|jantrienes___nereval                    |3037        |
|mpetazzoni___sseclient                  |3118        |
|troublegum___micropyserver              |3128        |
|hegusung___AVSignSeek                   |3197        |
|jtauber___blockchain                    |3213        |
|porimol___countryinfo                   |3285        |
|Bogdanp___cursive_re                    |3456        |
|patx___pickledb                         |3487        |
|nytimes___rd-blender-docker             |3517        |
|bsolomon1124___demoji                   |3554        |
|tdda___applehealthdata                  |3641        |
|skorokithakis___shortuuid               |3722        |
|pdftables___python-pdftables-api        |3762        |
|sighalt___logdecorator                  |3932        |
|SirAnthony___slpp                       |4117        |
|marteinn___The-Big-Username-Blocklist   |4333        |
|kevink1103___pyprnt                     |4359        |
|lionheart___pinboard.py                 |4366        |
|ross___requests-futures                 |4607        |
|zach-taylor___splunk_handler            |4641        |
|pwaller___pyprof2calltree               |4645        |
|italorossi___ishell                     |4734        |
|comadan___FM_FTRL                       |4866        |
|dorkitude___dstruct                     |5290        |
|disqus___python-phabricator             |5434        |
|dogsheep___swarm-to-sqlite              |5521        |
|naiyt___steamapiwrapper                 |5797        |
|ramazanpolat___prodict                  |5895        |
|ActiveState___appdirs                   |6164        |
|zestyping___q                           |6296        |
|imbal___safeyaml                        |6328        |
|nathanlct___reeds-shepp-curves          |6461        |
|r-kan___semile                          |6472        |
|riga___pymitter                         |6525        |
|zachwill___moment                       |6557        |
|ppannuto___python-titlecase             |6591        |
|stephenbradshaw___hlextend              |6646        |
|olle___lz77-kit                         |6868        |
|AWegnerGitHub___stackapi                |6942        |
|tenthirtyone___blocktools               |7003        |
|slomkowski___nginx-config-formatter     |7062        |
|sbyrnes321___numericalunits             |7518        |
|tikitu___jsmin                          |8004        |
|DigitaleGesellschaft___Anonip           |8024        |
|shinux___PyTime                         |8623        |
|ryancox___motionless                    |8989        |
|SteinRobert___python-restcountries      |9289        |
|exentriquesolutions___nip.io            |10099       |
|drewkerrigan___nagios-http-json         |10138       |
|ArturSpirin___pyPS4Controller           |10445       |
|100___Solid                             |10731       |
|stepchowfun___theorem-prover            |11097       |
|tasdikrahman___vocabulary               |11132       |
|luno___luno-python                      |11672       |
|dirn___When.py                          |12360       |
|jeffbuttars___cowpy                     |12548       |
|yaleimeng___Final_word_Similarity       |14662       |
|mk-fg___pretty-yaml                     |14838       |
|pglass___cube                           |19721       |
|pe-st___garmin-connect-export           |19806       |
|Hyun-je___pyrplidar                     |22274       |
|alecthomas___voluptuous                 |22599       |
|serge-sans-paille___gast                |28168       |
|nlitsme___pyidbutil                     |29803       |
|qedus___sphere                          |47222       |
|pyannote___pyannote-core                |66875       |


## Setup

- Download the repositories from https://github.com/DeepSoftwareAnalytics/RepoTransBench and put them in the `repos` directory.
- Each repo contains a `.git` that might confuse your editor. Execute `remove_git_info.sh` to remove them all and maybe restart your editor.
- Install uv and run the script with `uv run count-tokens.py`
