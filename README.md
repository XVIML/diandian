DRVI is a collection of virtual instrument widgets built upon Tkinter, NumPy, SciPy and Matplotlib. It also includes an app designer and several demonstration examples.

You can locate the `.whl` package on PyPI by searching for the keyword "drvi". Download the wheel compatible with your Python version, for example `drvi-0.9.3-py311-none-any.whl`

<img width="2270" height="1237" alt="image" src="https://github.com/user-attachments/assets/3803794a-ead5-44a5-abab-70f8a397fed2" />




Usually, it fails to find a suitable version for installation, and I’m not sure why:

pip install drvi

You will need to download the correct version manually.

<img width="2222" height="1729" alt="image" src="https://github.com/user-attachments/assets/dc8bd8d6-7360-44e5-8491-6d2b34db8265" />


Then install it using the command below:

pip install drvi-0.9.3-py311-none-any.whl

Several third-party packages are required. Install these dependencies prior to DRVI:

pip install numpy

pip install scipy

pip install matplotlib

pip install pyaudio

pip install sounddevice

pip install pyserial

pip install librosa

To try DRVI, download `TestDRVI.zip`, extract it to a local directory, such as 'd:\temp'. And run the included Python scripts. These programs use 'drvi' to build graphical user interfaces.

<img width="1524" height="537" alt="image" src="https://github.com/user-attachments/assets/88043275-3669-47a8-b626-42df086a052a" />



One example is `Example_Piano`, a virtual piano that generates pure tones, displays their waveforms and spectra, and plays audio.

<img width="2224" height="1435" alt="image" src="https://github.com/user-attachments/assets/fbcac93a-1268-4306-ae87-811879ee803a" />


