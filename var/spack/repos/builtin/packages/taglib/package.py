# Copyright (c) 2018 Mateusz Bysiek

from spack import *


class Taglib(CMakePackage):
    """TagLib is a library for reading and editing the meta-data of several popular audio formats.
    Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags
    and Vorbis comments in FLAC, MPC, Speex, WavPack, TrueAudio, WAV, AIFF, MP4 and ASF files.
    """

    homepage = "https://taglib.org/"
    git      = "https://github.com/taglib/taglib.git"

    url      = "https://taglib.org/releases/taglib-1.11.1.tar.gz"
    list_url = "https://taglib.org/releases/"
    list_depth = 1

    version('1.11.1', sha256='b6d1a5a610aae6ff39d93de5efd0fdc787aa9e9dc1e7026fa4c961b26563526b')
    version('1.11', sha256='ed4cabb3d970ff9a30b2620071c2b054c4347f44fc63546dbe06f97980ece288')
    version('1.10', sha256='24c32d50042cb0ddf162eb263f8ac75c5a158e12bf32ed534c1d5c71ee369baa')

    version('master', branch='master')

    # Config options
    #variant('zlib',          default=True,
    #        description='Build with zlib support')

    # Build dependencies
    depends_on('zlib')
    depends_on('cmake',  type='build')

    # def cmake_is_on(self, option):
    #     return 'ON' if option in self.spec else 'OFF'

    #         '-DUSE_XSDK_DEFAULTS=ON',
    #         '-DDIM:STRING=%s' % self.spec.variants['dimensions'].value,
    #         '-DBUILD_SHARED_LIBS:BOOL=%s' % self.cmake_is_on('+shared'),
    #         '-DENABLE_MPI:BOOL=%s' % self.cmake_is_on('+mpi'),
    #         '-DENABLE_OMP:BOOL=%s' % self.cmake_is_on('+openmp'),
    #         '-DXSDK_PRECISION:STRING=%s' %
    #         self.spec.variants['precision'].value.upper(),
    #         '-DENABLE_EB:BOOL=%s' % self.cmake_is_on('+eb'),
    #         '-DXSDK_ENABLE_Fortran:BOOL=%s' % self.cmake_is_on('+fortran'),
    #         '-DENABLE_LINEAR_SOLVERS:BOOL=%s' %
    #         self.cmake_is_on('+linear_solvers'),
    #         '-DENABLE_AMRDATA:BOOL=%s' % self.cmake_is_on('+amrdata'),
    #         '-DENABLE_PARTICLES:BOOL=%s' % self.cmake_is_on('+particles')
    def cmake_args(self):
        args = [
            '-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=true']
        # if '+zlib' in self.spec:
        #    args['-DZLIB_ROOT= ']
        return args
