# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


# class Amrex(CMakePackage):
class Amrex(AutotoolsPackage):
    """AMReX is a publicly available software framework designed
    for building massively parallel block- structured adaptive
    mesh refinement (AMR) applications."""

    homepage = "https://amrex-codes.github.io/amrex/"
    git      = "https://github.com/AMReX-Codes/amrex.git"

    url      = "https://github.com/AMReX-Codes/amrex/archive/18.10.1.zip"
    list_url = "https://github.com/AMReX-Codes/amrex/archive/"
    list_depth = 1

    version('develop', branch='development')
    version('18.10.1', commit='260b53169badaa760b91dfc60ea6b2ea3d9ccf06')  # tag:18.10.1
    version('18.10', commit='d37a266c38092e1174096e245326e9eead1f4e03')  # tag:18.10
    version('18.09.1', commit='88120db4736c325a2d3d2c291adacaffd3bf224b')  # tag:18.09.1
    version('master', branch='master')

    # Config options
    variant('dimensions', default='3',
            description='Dimensionality', values=('2', '3'))
    # variant('shared',  default=False,
    #         description='Build shared library')
    variant('mpi',          default=True,
            description='Build with MPI support')
    variant('openmp',       default=False,
            description='Build with OpenMP support')
    # variant('precision',  default='double',
    #         description='Real precision (double/single)',
    #         values=('single', 'double'))
    # variant('eb',  default=False,
    #         description='Build Embedded Boundary classes')
    variant('fortran',  default=False,
            description='Build Fortran API')
    variant('linear_solvers', default=True,
            description='Build linear solvers')
    # variant('amrdata',    default=False,
    #         description='Build data services')
    variant('particles',  default=False,
            description='Build particle classes')
    # variant('build_type', default='Release',
    #         description='The build type to build',
    #         values=('Debug', 'Release'))

    # Build dependencies
    depends_on('mpi', when='+mpi')
    # depends_on('python@2.7:', type='build')
    # depends_on('cmake@3.5:',  type='build')
    conflicts('%clang')

    def _yes_no(self, option):
        return 'yes' if option in self.spec else 'no'

    def configure_args(self):
        return [
            '--dim', str(self.spec.variants['dimensions'].value),
            '--with-mpi', self._yes_no('+mpi'),
            '--with-omp', self._yes_no('+openmp'),
            '--debug', 'no',
            # '--debug', 'yes' if self.spec['build_type'] == 'Debug' else 'no',
            '--enable-particle', self._yes_no('+particles'),
            '--enable-fortran-api', self._yes_no('+fortran'),
            '--enable-linear-solver', self._yes_no('+linear_solvers'),
            '--enable-xsdk-defaults', 'yes']

    # def cmake_is_on(self, option):
    #     return 'ON' if option in self.spec else 'OFF'

    # def cmake_args(self):
    #     args = [
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
    #     ]
    #     return args
