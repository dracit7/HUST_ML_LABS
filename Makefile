
PYTHON := $(shell if python -V 2>&1 | grep '3.' >/dev/null 2>&1;\
	then echo 'python';\
	elif python3 -V 2>&1 >/dev/null;\
	then echo 'python3';\
	else echo 'Error: can not find python3 on your system.' 1>&2; exit 1; fi\
)

VENVDIR := venv
IMGDIR := tmp/img
PIP_TIMEOUT := 1000

setup:
	mkdir -p $(IMGDIR)
	@echo Setting up python...
	@(\
		if ls $(VENVDIR) 2>/dev/null >/dev/null;\
		then echo - Found venv in $(VENVDIR).;\
		else echo - venv not set. Creating a new one...;\
		$(PYTHON) -m venv $(VENVDIR);\
		echo - Upgrading pip...;\
		pip install --upgrade pip >/dev/null;\
		fi;\
		. $(VENVDIR)/bin/activate;\
		if $(PYTHON) -c "import matplotlib" 2>/dev/null;\
		then echo - Found matplotlib in venv.;\
		else echo - Missing library matplotlib, installing...;\
			if $(PYTHON) -m pip $(PROXY) --default-timeout=$(PIP_TIMEOUT) install matplotlib;\
			then echo - installed matplotlib.;\
			else echo - installation failed.; exit 1; fi;\
		fi;\
		if $(PYTHON) -c "import numpy" 2>/dev/null;\
		then echo - Found numpy in venv.;\
		else echo - Missing library numpy, installing...;\
			if $(PYTHON) -m pip $(PROXY) --default-timeout=$(PIP_TIMEOUT) install numpy;\
			then echo - installed numpy.;\
			else echo - installation failed.; exit 1; fi;\
		fi;\
	)