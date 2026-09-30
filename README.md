DRVI is a collection of virtual instrument widgets built upon Tkinter, NumPy, SciPy and Matplotlib. It also includes an app designer and several demonstration examples.

You can locate the `.whl` package on PyPI by searching for the keyword "drvi". Download the wheel compatible with your Python version, for example `drvi-0.9.3-py311-none-any.whl`, then install it using the command below:

pip install drvi-0.9.3-py311-none-any.whl

Several third-party packages are required. Install these dependencies prior to DRVI:

pip install numpy

pip install scipy

pip install matplotlib

pip install pyaudio

pip install sounddevice

pip install pyserial

pip install librosa


To try DRVI, download `TestDRVI.zip`, extract it to a local directory, such as 'd:\temp'. And run the included Python scripts. These programs use drvi to build graphical user interfaces.

One example is `Example_Piano`, a virtual piano that generates pure tones, displays their waveforms and spectra, and plays audio.


