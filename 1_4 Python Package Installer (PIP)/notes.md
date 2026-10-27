# Install pip

## pip on MS Windows

- Verify whether pip is installed with:

```cmd
pip --version
```

- Also verify python directory is present in <code>$env:PATH</code>
  
```cmd
> ($env:PATH).Split(';')
C:\WINDOWS\system32
C:\WINDOWS
C:\WINDOWS\System32\Wbem
C:\WINDOWS\System32\WindowsPowerShell\v1.0\
C:\WINDOWS\System32\OpenSSH\
C:\Windows\install\it-tools\bin
C:\Users\ammiel.soriano\AppData\Local\Microsoft\WindowsApps
C:\Users\ammiel.soriano\AppData\Local\Programs\Microsoft VS Code\bin
C:\Users\ammiel.soriano\AppData\Local\Python\bin
c:\Users\ammiel.soriano\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\scripts\noConfigScripts
```

## pip on Linux

- Different Linux distrobutions may have python by default and may have concurrent versions available
- Verify either <code>pip --version</code> or <code>pip3 --version</code>
- If python exists, but pip is not included you can install pip using a <i>package manager(ie. apt)</i> or <code>python</code> itself
```bash
sudo apt install python3-pip
```

# Dependencies

## How to use pip

```cmd
> pip --help

Usage:   
  pip.exe <command> [options]

Commands:
  install                     Install packages.
  lock                        Generate a lock file.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [auto, disabled, import, subprocess]. (default: auto)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --no-proxy-env              Do not read proxy configuration from environment variables.
  --retries <retries>         Maximum attempts to establish a new HTTP connection. (default: 5)
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
  --resume-retries <resume_retries>
                              Maximum attempts to resume or restart an incomplete download. (default: 5)
```

- You can use <code>pip help \<command\></code> for more information
- Generally you can reference above codeblock or for full details https://pip.pypa.io/en/stable/

# Simple test program

- Python 3.14.x does not seem to be compatible with pygame

# Section Summary

<body> 
1. A repository (or repo for short) designed to collect and share free Python code exists and works under the name Python Package Index (PyPI) although it's also likely that you come across the very niche name The Cheese Shop. The Shop's website is available at https://pypi.org/.<br><br>
2. To make use of The Cheese Shop, a specialized tool has been created and its name is pip (pip installs packages while pip stands for... ok, never mind). As pip may not be deployed as a part of the standard Python installation, it is possible that you will need to install it manually. Pip is a console tool.<br><br>
3. To check pip's version one the following commands should be issued:

<code>pip --version</code>
 
<b>or</b>

<code>pip3 --version</code>

Check yourself which of these works for you in your OS's environment.<br><br>
4. The list of the main pip activities looks as follows:

<code>pip help \<command\></code> <br>– shows a brief description of pip;

<code>pip list </code> <br>– shows a list of the currently installed packages;

<code>pip show \<package\> </code><br>– shows package_name info including the package's dependencies;

<code>pip search \<string\> </code><br>– searches through PyPI directories in order to find packages whose names contain anystring;

<code>pip install \<package\> </code><br>– installs name system-wide (expect problems when you don't have administrative rights);

<code>pip install --user \<package\> </code><br>– installs name for you only; no other platform user will be able to use it;

<code>pip install -U \<package\> </code><br>– updates a previously installed package;

<code>pip uninstall \<package\> </code><br>– uninstalls a previously installed package.


# Quiz

<h3>
    Question 1:<br>
    Where does the name "The Cheese Shop" come from?<br><br>
    Answer:
</h3>
    It's a reference to an old Monty Python's sketch of the same name.
<h3>
    Question 2:<br>
    Why should I ensure which one of pip and pip3 works for me?<br><br>
    Answer:
</h3>
When Python 2 and Python 3 coexist in your OS, it's likely that pip identifies the instance of pip working with Python 2 packages only.

<h3>
    Question 3:<br>
    How can I determine if my pip works with either Python 2 or Python 3?<br><br>
    Answer:
</h3>

```cmd
pip --version will tell you that.
```

<h3>
    Question 4:<br>
    Unfortunately, I don't have administrative right. What should I do to install a package system-wide?<br><br>
    Answer:
</h3>
You have to ask your sysadmin - don't try to hack your OS!