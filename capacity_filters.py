import numpy
from numpy import atleast_1d,append,real,prod,zeros,concatenate,sqrt


def get_degree(z, p):

    degree = len(p) - len(z)

    return degree

def _zpklp2lp(z, p, k, wo=1.0):
    """
 Transform a lowpass filter prototype to a different frequency.
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
    :param z:Zeros of the analog IIR filter transfer function.
    :param p: Poles of the analog IIR filter transfer function.
    :param k: System gain of the analog IIR filter transfer function.
    :param wo: Desired cutoff, as angular frequency (e.g. rad/s).
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = get_degree(z, p)

    z_lp = wo * z
    p_lp = wo * p
    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp


def _zpklp2lp(z, p, k, wo=1.0):
    """
Transform a lowpass filter prototype to a different frequency.

    :param z: Zeros of the analog IIR filter transfer function.
    :param p: Poles of the analog IIR filter transfer function.
    :param k: System gain of the analog IIR filter transfer function
    :param wo: Desired cutoff, as angular frequency (e.g. rad/s).
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = get_degree(z, p)


    z_lp = wo * z
    p_lp = wo * p


    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp

def _zpklp2hp(z, p, k, wo=1.0):
    """
Transform a lowpass filter prototype to a highpass filter.
    :param z:
    :param p:
    :param k:
    :param wo:
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = get_degree(z, p)


    z_hp = wo / z
    p_hp = wo / p


    z_hp = append(z_hp, zeros(degree))


    k_hp = k * real(prod(-z) / prod(-p))

    return z_hp, p_hp, k_hp


def _zpklp2lp(z, p, k, wo=1.0):
    """
Transform a lowpass filter prototype to a different frequency.
    :param z:
    :param p:
    :param k:
    :param wo:
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = get_degree(z, p)


    z_lp = wo * z
    p_lp = wo * p


    k_lp = k * wo**degree

    return z_lp, p_lp, k_lp


def _zpklp2hp(z, p, k, wo=1.0):
    """
Transform a lowpass filter prototype to a highpass filter.
    :param z:
    :param p:
    :param k:
    :param wo:
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)

    degree = get_degree(z, p)


    z_hp = wo / z
    p_hp = wo / p


    z_hp = append(z_hp, zeros(degree))


    k_hp = k * real(prod(-z) / prod(-p))

    return z_hp, p_hp, k_hp


def _zpklp2bp(z, p, k, wo=1.0, bw=1.0):
    """
Transform a lowpass filter prototype to a bandpass filter.
    :param z:
    :param p:
    :param k:
    :param wo:
    :param bw:
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    wo = float(wo)
    bw = float(bw)

    degree = get_degree(z, p)


    z_lp = z * bw/2
    p_lp = p * bw/2


    z_lp = z_lp.astype(complex)
    p_lp = p_lp.astype(complex)


    z_bp = concatenate((z_lp + sqrt(z_lp**2 - wo**2),
                        z_lp - sqrt(z_lp**2 - wo**2)))
    p_bp = concatenate((p_lp + sqrt(p_lp**2 - wo**2),
                        p_lp - sqrt(p_lp**2 - wo**2)))


    z_bp = append(z_bp, zeros(degree))


    k_bp = k * bw**degree

    return z_bp, p_bp, k_bp


def _zpklp2bs(z, p, k, wo=1.0, bw=1.0):
    """
Transform a lowpass filter prototype to a bandstop filter.
    :param z:
    :param p:
    :param k:
    :param wo:
    :param bw:
    :return:
    """
    z = numpy.atleast_1d(z)
    p = numpy.atleast_1d(p)
    wo = float(wo)
    bw = float(bw)

    degree = len(p) - len(z)


    z_hp = (bw/2) / z
    p_hp = (bw/2) / p


    z_hp = z_hp.astype(complex)
    p_hp = p_hp.astype(complex)


    z_bs = numpy.concatenate((z_hp + numpy.sqrt(z_hp**2 - wo**2),
                        z_hp - numpy.sqrt(z_hp**2 - wo**2)))
    p_bs = numpy.concatenate((p_hp + numpy.sqrt(p_hp**2 - wo**2),
                        p_hp - numpy.sqrt(p_hp**2 - wo**2)))


    z_bs = numpy.append(z_bs, +1j*wo * numpy.ones(degree))
    z_bs = numpy.append(z_bs, -1j*wo * numpy.ones(degree))

    k_bs = k * numpy.real(numpy.prod(-z) / numpy.prod(-p))

    return z_bs, p_bs, k_bs

def _zpkbilinear(z, p, k, fs):
    """
Return a digital filter from an analog one using a bilinear transform.
    :param z:
    :param p:
    :param k:
    :param fs:
    :return:
    """
    z = atleast_1d(z)
    p = atleast_1d(p)
    degree = get_degree(z, p)

    fs2 = 2*fs
    z_z = (fs2 + z) / (fs2 - z)
    p_z = (fs2 + p) / (fs2 - p)
    z_z = append(z_z, -numpy.core.numeric.ones(degree))
    k_z = k * real(prod(fs2 - z) / prod(fs2 - p))

    return z_z, p_z, k_z
