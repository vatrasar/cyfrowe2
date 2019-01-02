import numpy
from numpy import atleast_1d,append,real,prod,zeros,concatenate,sqrt
from scipy import signal

def _relative_degree(z, p):
    """
    Return relative degree of transfer function from zeros and poles
    """
    degree = len(p) - len(z)
    if degree < 0:
        raise ValueError("Improper transfer function. "
                         "Must have at least as many poles as zeros.")
    else:
        return degree


# TODO: merge these into existing functions or make public versions


def _zpklp2lp(z, p, k, wo=1.0):
    r"""
    Transform a lowpass filter prototype to a different frequency.

    Return an analog low-pass filter with cutoff frequency `wo`
    from an analog low-pass filter prototype with unity cutoff frequency,
    using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired cutoff, as angular frequency (e.g. rad/s).
        Defaults to no change.

    Returns
    -------
    z : ndarray
        Zeros of the transformed low-pass filter transfer function.
    p : ndarray
        Poles of the transformed low-pass filter transfer function.
    k : float
        System gain of the transformed low-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{s}{\omega_0}

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)  # Avoid int wraparound

    degree = _relative_degree(z, p)

    # Scale all points radially from origin to shift cutoff frequency
    z_lp = wo * z
    p_lp = wo * p

    # Each shifted pole decreases gain by wo, each shifted zero increases it.
    # Cancel out the net change to keep overall gain the same
    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp


def _zpklp2lp(z, p, k, wo=1.0):
    r"""
    Transform a lowpass filter prototype to a different frequency.

    Return an analog low-pass filter with cutoff frequency `wo`
    from an analog low-pass filter prototype with unity cutoff frequency,
    using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired cutoff, as angular frequency (e.g. rad/s).
        Defaults to no change.

    Returns
    -------
    z : ndarray
        Zeros of the transformed low-pass filter transfer function.
    p : ndarray
        Poles of the transformed low-pass filter transfer function.
    k : float
        System gain of the transformed low-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{s}{\omega_0}

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)  # Avoid int wraparound

    degree = _relative_degree(z, p)

    # Scale all points radially from origin to shift cutoff frequency
    z_lp = wo * z
    p_lp = wo * p

    # Each shifted pole decreases gain by wo, each shifted zero increases it.
    # Cancel out the net change to keep overall gain the same
    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp

def _zpklp2hp(z, p, k, wo=1.0):
    r"""
    Transform a lowpass filter prototype to a highpass filter.

    Return an analog high-pass filter with cutoff frequency `wo`
    from an analog low-pass filter prototype with unity cutoff frequency,
    using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired cutoff, as angular frequency (e.g. rad/s).
        Defaults to no change.

    Returns
    -------
    z : ndarray
        Zeros of the transformed high-pass filter transfer function.
    p : ndarray
        Poles of the transformed high-pass filter transfer function.
    k : float
        System gain of the transformed high-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{\omega_0}{s}

    This maintains symmetry of the lowpass and highpass responses on a
    logarithmic scale.

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = _relative_degree(z, p)

    # Invert positions radially about unit circle to convert LPF to HPF
    # Scale all points radially from origin to shift cutoff frequency
    z_hp = wo / z
    p_hp = wo / p

    # If lowpass had zeros at infinity, inverting moves them to origin.
    z_hp = append(z_hp, zeros(degree))

    # Cancel out gain change caused by inversion
    k_hp = k * real(prod(-z) / prod(-p))

    return z_hp, p_hp, k_hp


def _zpklp2lp(z, p, k, wo=1.0):
    r"""
    Transform a lowpass filter prototype to a different frequency.

    Return an analog low-pass filter with cutoff frequency `wo`
    from an analog low-pass filter prototype with unity cutoff frequency,
    using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired cutoff, as angular frequency (e.g. rad/s).
        Defaults to no change.

    Returns
    -------
    z : ndarray
        Zeros of the transformed low-pass filter transfer function.
    p : ndarray
        Poles of the transformed low-pass filter transfer function.
    k : float
        System gain of the transformed low-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{s}{\omega_0}

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)  # Avoid int wraparound

    degree = _relative_degree(z, p)

    # Scale all points radially from origin to shift cutoff frequency
    z_lp = wo * z
    p_lp = wo * p

    # Each shifted pole decreases gain by wo, each shifted zero increases it.
    # Cancel out the net change to keep overall gain the same
    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp


def _zpklp2hp(z, p, k, wo=1.0):
    r"""
    Transform a lowpass filter prototype to a highpass filter.

    Return an analog high-pass filter with cutoff frequency `wo`
    from an analog low-pass filter prototype with unity cutoff frequency,
    using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired cutoff, as angular frequency (e.g. rad/s).
        Defaults to no change.

    Returns
    -------
    z : ndarray
        Zeros of the transformed high-pass filter transfer function.
    p : ndarray
        Poles of the transformed high-pass filter transfer function.
    k : float
        System gain of the transformed high-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{\omega_0}{s}

    This maintains symmetry of the lowpass and highpass responses on a
    logarithmic scale.

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = _relative_degree(z, p)

    # Invert positions radially about unit circle to convert LPF to HPF
    # Scale all points radially from origin to shift cutoff frequency
    z_hp = wo / z
    p_hp = wo / p

    # If lowpass had zeros at infinity, inverting moves them to origin.
    z_hp = append(z_hp, zeros(degree))

    # Cancel out gain change caused by inversion
    k_hp = k * real(prod(-z) / prod(-p))

    return z_hp, p_hp, k_hp


def _zpklp2bp(z, p, k, wo=1.0, bw=1.0):
    r"""
    Transform a lowpass filter prototype to a bandpass filter.

    Return an analog band-pass filter with center frequency `wo` and
    bandwidth `bw` from an analog low-pass filter prototype with unity
    cutoff frequency, using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired passband center, as angular frequency (e.g. rad/s).
        Defaults to no change.
    bw : float
        Desired passband width, as angular frequency (e.g. rad/s).
        Defaults to 1.

    Returns
    -------
    z : ndarray
        Zeros of the transformed band-pass filter transfer function.
    p : ndarray
        Poles of the transformed band-pass filter transfer function.
    k : float
        System gain of the transformed band-pass filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{s^2 + {\omega_0}^2}{s \cdot \mathrm{BW}}

    This is the "wideband" transformation, producing a passband with
    geometric (log frequency) symmetry about `wo`.

    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)
    bw = float(bw)

    degree = _relative_degree(z, p)

    # Scale poles and zeros to desired bandwidth
    z_lp = z * bw/2
    p_lp = p * bw/2

    # Square root needs to produce complex result, not NaN
    z_lp = z_lp.astype(complex)
    p_lp = p_lp.astype(complex)

    # Duplicate poles and zeros and shift from baseband to +wo and -wo
    z_bp = concatenate((z_lp + sqrt(z_lp**2 - wo**2),
                        z_lp - sqrt(z_lp**2 - wo**2)))
    p_bp = concatenate((p_lp + sqrt(p_lp**2 - wo**2),
                        p_lp - sqrt(p_lp**2 - wo**2)))

    # Move degree zeros to origin, leaving degree zeros at infinity for BPF
    z_bp = append(z_bp, zeros(degree))

    # Cancel out gain change from frequency scaling
    k_bp = k * bw**degree

    return z_bp, p_bp, k_bp


def _zpklp2bs(z, p, k, wo=1.0, bw=1.0):
    r"""
    Transform a lowpass filter prototype to a bandstop filter.

    Return an analog band-stop filter with center frequency `wo` and
    stopband width `bw` from an analog low-pass filter prototype with unity
    cutoff frequency, using zeros, poles, and gain ('zpk') representation.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    wo : float
        Desired stopband center, as angular frequency (e.g. rad/s).
        Defaults to no change.
    bw : float
        Desired stopband width, as angular frequency (e.g. rad/s).
        Defaults to 1.

    Returns
    -------
    z : ndarray
        Zeros of the transformed band-stop filter transfer function.
    p : ndarray
        Poles of the transformed band-stop filter transfer function.
    k : float
        System gain of the transformed band-stop filter.

    Notes
    -----
    This is derived from the s-plane substitution

    .. math:: s \rightarrow \frac{s \cdot \mathrm{BW}}{s^2 + {\omega_0}^2}

    This is the "wideband" transformation, producing a stopband with
    geometric (log frequency) symmetry about `wo`.

    """
    z = numpy.atleast_1d(z)
    p = numpy.atleast_1d(p)
    wo = float(wo)
    bw = float(bw)

    degree = len(p) - len(z)

    # Invert to a highpass filter with desired bandwidth
    z_hp = (bw/2) / z
    p_hp = (bw/2) / p

    # Square root needs to produce complex result, not NaN
    z_hp = z_hp.astype(complex)
    p_hp = p_hp.astype(complex)

    # Duplicate poles and zeros and shift from baseband to +wo and -wo
    z_bs = numpy.concatenate((z_hp + numpy.sqrt(z_hp**2 - wo**2),
                        z_hp - numpy.sqrt(z_hp**2 - wo**2)))
    p_bs = numpy.concatenate((p_hp + numpy.sqrt(p_hp**2 - wo**2),
                        p_hp - numpy.sqrt(p_hp**2 - wo**2)))

    # Move any zeros that were at infinity to the center of the stopband
    z_bs = numpy.append(z_bs, +1j*wo * numpy.ones(degree))
    z_bs = numpy.append(z_bs, -1j*wo * numpy.ones(degree))

    # Cancel out gain change caused by inversion
    k_bs = k * numpy.real(numpy.prod(-z) / numpy.prod(-p))

    return z_bs, p_bs, k_bs

def _zpkbilinear(z, p, k, fs):
    """
    Return a digital filter from an analog one using a bilinear transform.

    Transform a set of poles and zeros from the analog s-plane to the digital
    z-plane using Tustin's method, which substitutes ``(z-1) / (z+1)`` for
    ``s``, maintaining the shape of the frequency response.

    Parameters
    ----------
    z : array_like
        Zeros of the analog IIR filter transfer function.
    p : array_like
        Poles of the analog IIR filter transfer function.
    k : float
        System gain of the analog IIR filter transfer function.
    fs : float
        Sample rate, as ordinary frequency (e.g. hertz). No prewarping is
        done in this function.

    Returns
    -------
    z : ndarray
        Zeros of the transformed digital filter transfer function.
    p : ndarray
        Poles of the transformed digital filter transfer function.
    k : float
        System gain of the transformed digital filter.

    """
    z = atleast_1d(z)
    p = atleast_1d(p)

    degree = _relative_degree(z, p)

    fs2 = 2*fs

    # Bilinear transform the poles and zeros
    z_z = (fs2 + z) / (fs2 - z)
    p_z = (fs2 + p) / (fs2 - p)

    # Any zeros that were at infinity get moved to the Nyquist frequency
    z_z = append(z_z, -numpy.numeric.ones(degree))

    # Compensate for gain change
    k_z = k * real(prod(fs2 - z) / prod(fs2 - p))

    return z_z, p_z, k_z
