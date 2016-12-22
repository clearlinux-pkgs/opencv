#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : opencv
Version  : 3.1.0
Release  : 11
URL      : https://github.com/Itseez/opencv/archive/3.1.0.tar.gz
Source0  : https://github.com/Itseez/opencv/archive/3.1.0.tar.gz
Summary  : Open Source Computer Vision Library
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear JasPer-2.0 LGPL-2.1 Libpng libtiff
Requires: opencv-bin
Requires: opencv-lib
Requires: opencv-python
Requires: opencv-data
BuildRequires : beignet-dev
BuildRequires : ccache
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-dev
BuildRequires : glib-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk3-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libva-dev
BuildRequires : libva-intel-driver
BuildRequires : mesa-dev
BuildRequires : numpy
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : pkgconfig(libpng)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : tbb-dev
BuildRequires : v4l-utils-dev
BuildRequires : zlib-dev

%description
A demo of the Java wrapper for OpenCV with two examples:
1) feature detection and matching and
2) face detection.
The examples are coded in Scala and Java.
Anyone familiar with Java should be able to read the Scala examples.
Please feel free to contribute code examples in Scala or Java, or any JVM language.

%package bin
Summary: bin components for the opencv package.
Group: Binaries
Requires: opencv-data

%description bin
bin components for the opencv package.


%package data
Summary: data components for the opencv package.
Group: Data

%description data
data components for the opencv package.


%package dev
Summary: dev components for the opencv package.
Group: Development
Requires: opencv-lib
Requires: opencv-bin
Requires: opencv-data
Provides: opencv-devel

%description dev
dev components for the opencv package.


%package lib
Summary: lib components for the opencv package.
Group: Libraries
Requires: opencv-data

%description lib
lib components for the opencv package.


%package python
Summary: python components for the opencv package.
Group: Default

%description python
python components for the opencv package.


%prep
%setup -q -n opencv-3.1.0

%build
export LANG=C
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=OFF -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=OFF -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_AVX2=ON -DENABLE_SSE42=ON  -DENABLE_AVX=ON -DCMAKE_LIBRARY_PATH=/lib64 -DWITH_TBB=on -DWITH_OPENMP=ON -DWITH_VA=ON -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1
make VERBOSE=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/opencv_annotation
/usr/bin/opencv_createsamples
/usr/bin/opencv_traincascade

%files data
%defattr(-,root,root,-)
/usr/share/OpenCV/OpenCVConfig-version.cmake
/usr/share/OpenCV/OpenCVConfig.cmake
/usr/share/OpenCV/OpenCVModules-releasewithdebinfo.cmake
/usr/share/OpenCV/OpenCVModules.cmake
/usr/share/OpenCV/haarcascades/haarcascade_eye.xml
/usr/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml
/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml
/usr/share/OpenCV/haarcascades/haarcascade_fullbody.xml
/usr/share/OpenCV/haarcascades/haarcascade_lefteye_2splits.xml
/usr/share/OpenCV/haarcascades/haarcascade_licence_plate_rus_16stages.xml
/usr/share/OpenCV/haarcascades/haarcascade_lowerbody.xml
/usr/share/OpenCV/haarcascades/haarcascade_profileface.xml
/usr/share/OpenCV/haarcascades/haarcascade_righteye_2splits.xml
/usr/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml
/usr/share/OpenCV/haarcascades/haarcascade_smile.xml
/usr/share/OpenCV/haarcascades/haarcascade_upperbody.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_silverware.xml
/usr/share/OpenCV/samples/python/_coverage.py
/usr/share/OpenCV/samples/python/_coverage.pyc
/usr/share/OpenCV/samples/python/_coverage.pyo
/usr/share/OpenCV/samples/python/_doc.py
/usr/share/OpenCV/samples/python/_doc.pyc
/usr/share/OpenCV/samples/python/_doc.pyo
/usr/share/OpenCV/samples/python/asift.py
/usr/share/OpenCV/samples/python/asift.pyc
/usr/share/OpenCV/samples/python/asift.pyo
/usr/share/OpenCV/samples/python/browse.py
/usr/share/OpenCV/samples/python/browse.pyc
/usr/share/OpenCV/samples/python/browse.pyo
/usr/share/OpenCV/samples/python/calibrate.py
/usr/share/OpenCV/samples/python/calibrate.pyc
/usr/share/OpenCV/samples/python/calibrate.pyo
/usr/share/OpenCV/samples/python/camshift.py
/usr/share/OpenCV/samples/python/camshift.pyc
/usr/share/OpenCV/samples/python/camshift.pyo
/usr/share/OpenCV/samples/python/coherence.py
/usr/share/OpenCV/samples/python/coherence.pyc
/usr/share/OpenCV/samples/python/coherence.pyo
/usr/share/OpenCV/samples/python/color_histogram.py
/usr/share/OpenCV/samples/python/color_histogram.pyc
/usr/share/OpenCV/samples/python/color_histogram.pyo
/usr/share/OpenCV/samples/python/common.py
/usr/share/OpenCV/samples/python/common.pyc
/usr/share/OpenCV/samples/python/common.pyo
/usr/share/OpenCV/samples/python/contours.py
/usr/share/OpenCV/samples/python/contours.pyc
/usr/share/OpenCV/samples/python/contours.pyo
/usr/share/OpenCV/samples/python/deconvolution.py
/usr/share/OpenCV/samples/python/deconvolution.pyc
/usr/share/OpenCV/samples/python/deconvolution.pyo
/usr/share/OpenCV/samples/python/demo.py
/usr/share/OpenCV/samples/python/demo.pyc
/usr/share/OpenCV/samples/python/demo.pyo
/usr/share/OpenCV/samples/python/dft.py
/usr/share/OpenCV/samples/python/dft.pyc
/usr/share/OpenCV/samples/python/dft.pyo
/usr/share/OpenCV/samples/python/digits.py
/usr/share/OpenCV/samples/python/digits.pyc
/usr/share/OpenCV/samples/python/digits.pyo
/usr/share/OpenCV/samples/python/digits_adjust.py
/usr/share/OpenCV/samples/python/digits_adjust.pyc
/usr/share/OpenCV/samples/python/digits_adjust.pyo
/usr/share/OpenCV/samples/python/digits_video.py
/usr/share/OpenCV/samples/python/digits_video.pyc
/usr/share/OpenCV/samples/python/digits_video.pyo
/usr/share/OpenCV/samples/python/distrans.py
/usr/share/OpenCV/samples/python/distrans.pyc
/usr/share/OpenCV/samples/python/distrans.pyo
/usr/share/OpenCV/samples/python/edge.py
/usr/share/OpenCV/samples/python/edge.pyc
/usr/share/OpenCV/samples/python/edge.pyo
/usr/share/OpenCV/samples/python/facedetect.py
/usr/share/OpenCV/samples/python/facedetect.pyc
/usr/share/OpenCV/samples/python/facedetect.pyo
/usr/share/OpenCV/samples/python/feature_homography.py
/usr/share/OpenCV/samples/python/feature_homography.pyc
/usr/share/OpenCV/samples/python/feature_homography.pyo
/usr/share/OpenCV/samples/python/find_obj.py
/usr/share/OpenCV/samples/python/find_obj.pyc
/usr/share/OpenCV/samples/python/find_obj.pyo
/usr/share/OpenCV/samples/python/fitline.py
/usr/share/OpenCV/samples/python/fitline.pyc
/usr/share/OpenCV/samples/python/fitline.pyo
/usr/share/OpenCV/samples/python/floodfill.py
/usr/share/OpenCV/samples/python/floodfill.pyc
/usr/share/OpenCV/samples/python/floodfill.pyo
/usr/share/OpenCV/samples/python/gabor_threads.py
/usr/share/OpenCV/samples/python/gabor_threads.pyc
/usr/share/OpenCV/samples/python/gabor_threads.pyo
/usr/share/OpenCV/samples/python/gaussian_mix.py
/usr/share/OpenCV/samples/python/gaussian_mix.pyc
/usr/share/OpenCV/samples/python/gaussian_mix.pyo
/usr/share/OpenCV/samples/python/grabcut.py
/usr/share/OpenCV/samples/python/grabcut.pyc
/usr/share/OpenCV/samples/python/grabcut.pyo
/usr/share/OpenCV/samples/python/hist.py
/usr/share/OpenCV/samples/python/hist.pyc
/usr/share/OpenCV/samples/python/hist.pyo
/usr/share/OpenCV/samples/python/houghcircles.py
/usr/share/OpenCV/samples/python/houghcircles.pyc
/usr/share/OpenCV/samples/python/houghcircles.pyo
/usr/share/OpenCV/samples/python/houghlines.py
/usr/share/OpenCV/samples/python/houghlines.pyc
/usr/share/OpenCV/samples/python/houghlines.pyo
/usr/share/OpenCV/samples/python/inpaint.py
/usr/share/OpenCV/samples/python/inpaint.pyc
/usr/share/OpenCV/samples/python/inpaint.pyo
/usr/share/OpenCV/samples/python/kalman.py
/usr/share/OpenCV/samples/python/kalman.pyc
/usr/share/OpenCV/samples/python/kalman.pyo
/usr/share/OpenCV/samples/python/kmeans.py
/usr/share/OpenCV/samples/python/kmeans.pyc
/usr/share/OpenCV/samples/python/kmeans.pyo
/usr/share/OpenCV/samples/python/lappyr.py
/usr/share/OpenCV/samples/python/lappyr.pyc
/usr/share/OpenCV/samples/python/lappyr.pyo
/usr/share/OpenCV/samples/python/letter_recog.py
/usr/share/OpenCV/samples/python/letter_recog.pyc
/usr/share/OpenCV/samples/python/letter_recog.pyo
/usr/share/OpenCV/samples/python/lk_homography.py
/usr/share/OpenCV/samples/python/lk_homography.pyc
/usr/share/OpenCV/samples/python/lk_homography.pyo
/usr/share/OpenCV/samples/python/lk_track.py
/usr/share/OpenCV/samples/python/lk_track.pyc
/usr/share/OpenCV/samples/python/lk_track.pyo
/usr/share/OpenCV/samples/python/logpolar.py
/usr/share/OpenCV/samples/python/logpolar.pyc
/usr/share/OpenCV/samples/python/logpolar.pyo
/usr/share/OpenCV/samples/python/morphology.py
/usr/share/OpenCV/samples/python/morphology.pyc
/usr/share/OpenCV/samples/python/morphology.pyo
/usr/share/OpenCV/samples/python/mosse.py
/usr/share/OpenCV/samples/python/mosse.pyc
/usr/share/OpenCV/samples/python/mosse.pyo
/usr/share/OpenCV/samples/python/mouse_and_match.py
/usr/share/OpenCV/samples/python/mouse_and_match.pyc
/usr/share/OpenCV/samples/python/mouse_and_match.pyo
/usr/share/OpenCV/samples/python/mser.py
/usr/share/OpenCV/samples/python/mser.pyc
/usr/share/OpenCV/samples/python/mser.pyo
/usr/share/OpenCV/samples/python/opencv_version.py
/usr/share/OpenCV/samples/python/opencv_version.pyc
/usr/share/OpenCV/samples/python/opencv_version.pyo
/usr/share/OpenCV/samples/python/opt_flow.py
/usr/share/OpenCV/samples/python/opt_flow.pyc
/usr/share/OpenCV/samples/python/opt_flow.pyo
/usr/share/OpenCV/samples/python/peopledetect.py
/usr/share/OpenCV/samples/python/peopledetect.pyc
/usr/share/OpenCV/samples/python/peopledetect.pyo
/usr/share/OpenCV/samples/python/plane_ar.py
/usr/share/OpenCV/samples/python/plane_ar.pyc
/usr/share/OpenCV/samples/python/plane_ar.pyo
/usr/share/OpenCV/samples/python/plane_tracker.py
/usr/share/OpenCV/samples/python/plane_tracker.pyc
/usr/share/OpenCV/samples/python/plane_tracker.pyo
/usr/share/OpenCV/samples/python/squares.py
/usr/share/OpenCV/samples/python/squares.pyc
/usr/share/OpenCV/samples/python/squares.pyo
/usr/share/OpenCV/samples/python/stereo_match.py
/usr/share/OpenCV/samples/python/stereo_match.pyc
/usr/share/OpenCV/samples/python/stereo_match.pyo
/usr/share/OpenCV/samples/python/texture_flow.py
/usr/share/OpenCV/samples/python/texture_flow.pyc
/usr/share/OpenCV/samples/python/texture_flow.pyo
/usr/share/OpenCV/samples/python/turing.py
/usr/share/OpenCV/samples/python/turing.pyc
/usr/share/OpenCV/samples/python/turing.pyo
/usr/share/OpenCV/samples/python/video.py
/usr/share/OpenCV/samples/python/video.pyc
/usr/share/OpenCV/samples/python/video.pyo
/usr/share/OpenCV/samples/python/video_threaded.py
/usr/share/OpenCV/samples/python/video_threaded.pyc
/usr/share/OpenCV/samples/python/video_threaded.pyo
/usr/share/OpenCV/samples/python/video_v4l2.py
/usr/share/OpenCV/samples/python/video_v4l2.pyc
/usr/share/OpenCV/samples/python/video_v4l2.pyo
/usr/share/OpenCV/samples/python/watershed.py
/usr/share/OpenCV/samples/python/watershed.pyc
/usr/share/OpenCV/samples/python/watershed.pyo

%files dev
%defattr(-,root,root,-)
/usr/include/opencv/cv.h
/usr/include/opencv/cv.hpp
/usr/include/opencv/cvaux.h
/usr/include/opencv/cvaux.hpp
/usr/include/opencv/cvwimage.h
/usr/include/opencv/cxcore.h
/usr/include/opencv/cxcore.hpp
/usr/include/opencv/cxeigen.hpp
/usr/include/opencv/cxmisc.h
/usr/include/opencv/highgui.h
/usr/include/opencv/ml.h
/usr/include/opencv2/calib3d.hpp
/usr/include/opencv2/calib3d/calib3d.hpp
/usr/include/opencv2/calib3d/calib3d_c.h
/usr/include/opencv2/core.hpp
/usr/include/opencv2/core/affine.hpp
/usr/include/opencv2/core/base.hpp
/usr/include/opencv2/core/bufferpool.hpp
/usr/include/opencv2/core/core.hpp
/usr/include/opencv2/core/core_c.h
/usr/include/opencv2/core/cuda.hpp
/usr/include/opencv2/core/cuda.inl.hpp
/usr/include/opencv2/core/cuda/block.hpp
/usr/include/opencv2/core/cuda/border_interpolate.hpp
/usr/include/opencv2/core/cuda/color.hpp
/usr/include/opencv2/core/cuda/common.hpp
/usr/include/opencv2/core/cuda/datamov_utils.hpp
/usr/include/opencv2/core/cuda/detail/color_detail.hpp
/usr/include/opencv2/core/cuda/detail/reduce.hpp
/usr/include/opencv2/core/cuda/detail/reduce_key_val.hpp
/usr/include/opencv2/core/cuda/detail/transform_detail.hpp
/usr/include/opencv2/core/cuda/detail/type_traits_detail.hpp
/usr/include/opencv2/core/cuda/detail/vec_distance_detail.hpp
/usr/include/opencv2/core/cuda/dynamic_smem.hpp
/usr/include/opencv2/core/cuda/emulation.hpp
/usr/include/opencv2/core/cuda/filters.hpp
/usr/include/opencv2/core/cuda/funcattrib.hpp
/usr/include/opencv2/core/cuda/functional.hpp
/usr/include/opencv2/core/cuda/limits.hpp
/usr/include/opencv2/core/cuda/reduce.hpp
/usr/include/opencv2/core/cuda/saturate_cast.hpp
/usr/include/opencv2/core/cuda/scan.hpp
/usr/include/opencv2/core/cuda/simd_functions.hpp
/usr/include/opencv2/core/cuda/transform.hpp
/usr/include/opencv2/core/cuda/type_traits.hpp
/usr/include/opencv2/core/cuda/utility.hpp
/usr/include/opencv2/core/cuda/vec_distance.hpp
/usr/include/opencv2/core/cuda/vec_math.hpp
/usr/include/opencv2/core/cuda/vec_traits.hpp
/usr/include/opencv2/core/cuda/warp.hpp
/usr/include/opencv2/core/cuda/warp_reduce.hpp
/usr/include/opencv2/core/cuda/warp_shuffle.hpp
/usr/include/opencv2/core/cuda_stream_accessor.hpp
/usr/include/opencv2/core/cuda_types.hpp
/usr/include/opencv2/core/cvdef.h
/usr/include/opencv2/core/cvstd.hpp
/usr/include/opencv2/core/cvstd.inl.hpp
/usr/include/opencv2/core/directx.hpp
/usr/include/opencv2/core/eigen.hpp
/usr/include/opencv2/core/fast_math.hpp
/usr/include/opencv2/core/hal/hal.hpp
/usr/include/opencv2/core/hal/interface.h
/usr/include/opencv2/core/hal/intrin.hpp
/usr/include/opencv2/core/hal/intrin_cpp.hpp
/usr/include/opencv2/core/hal/intrin_neon.hpp
/usr/include/opencv2/core/hal/intrin_sse.hpp
/usr/include/opencv2/core/ippasync.hpp
/usr/include/opencv2/core/mat.hpp
/usr/include/opencv2/core/mat.inl.hpp
/usr/include/opencv2/core/matx.hpp
/usr/include/opencv2/core/neon_utils.hpp
/usr/include/opencv2/core/ocl.hpp
/usr/include/opencv2/core/ocl_genbase.hpp
/usr/include/opencv2/core/opengl.hpp
/usr/include/opencv2/core/operations.hpp
/usr/include/opencv2/core/optim.hpp
/usr/include/opencv2/core/persistence.hpp
/usr/include/opencv2/core/private.cuda.hpp
/usr/include/opencv2/core/private.hpp
/usr/include/opencv2/core/ptr.inl.hpp
/usr/include/opencv2/core/saturate.hpp
/usr/include/opencv2/core/sse_utils.hpp
/usr/include/opencv2/core/traits.hpp
/usr/include/opencv2/core/types.hpp
/usr/include/opencv2/core/types_c.h
/usr/include/opencv2/core/utility.hpp
/usr/include/opencv2/core/va_intel.hpp
/usr/include/opencv2/core/version.hpp
/usr/include/opencv2/core/wimage.hpp
/usr/include/opencv2/cvconfig.h
/usr/include/opencv2/features2d.hpp
/usr/include/opencv2/features2d/features2d.hpp
/usr/include/opencv2/flann.hpp
/usr/include/opencv2/flann/all_indices.h
/usr/include/opencv2/flann/allocator.h
/usr/include/opencv2/flann/any.h
/usr/include/opencv2/flann/autotuned_index.h
/usr/include/opencv2/flann/composite_index.h
/usr/include/opencv2/flann/config.h
/usr/include/opencv2/flann/defines.h
/usr/include/opencv2/flann/dist.h
/usr/include/opencv2/flann/dummy.h
/usr/include/opencv2/flann/dynamic_bitset.h
/usr/include/opencv2/flann/flann.hpp
/usr/include/opencv2/flann/flann_base.hpp
/usr/include/opencv2/flann/general.h
/usr/include/opencv2/flann/ground_truth.h
/usr/include/opencv2/flann/hdf5.h
/usr/include/opencv2/flann/heap.h
/usr/include/opencv2/flann/hierarchical_clustering_index.h
/usr/include/opencv2/flann/index_testing.h
/usr/include/opencv2/flann/kdtree_index.h
/usr/include/opencv2/flann/kdtree_single_index.h
/usr/include/opencv2/flann/kmeans_index.h
/usr/include/opencv2/flann/linear_index.h
/usr/include/opencv2/flann/logger.h
/usr/include/opencv2/flann/lsh_index.h
/usr/include/opencv2/flann/lsh_table.h
/usr/include/opencv2/flann/matrix.h
/usr/include/opencv2/flann/miniflann.hpp
/usr/include/opencv2/flann/nn_index.h
/usr/include/opencv2/flann/object_factory.h
/usr/include/opencv2/flann/params.h
/usr/include/opencv2/flann/random.h
/usr/include/opencv2/flann/result_set.h
/usr/include/opencv2/flann/sampling.h
/usr/include/opencv2/flann/saving.h
/usr/include/opencv2/flann/simplex_downhill.h
/usr/include/opencv2/flann/timer.h
/usr/include/opencv2/highgui.hpp
/usr/include/opencv2/highgui/highgui.hpp
/usr/include/opencv2/highgui/highgui_c.h
/usr/include/opencv2/imgcodecs.hpp
/usr/include/opencv2/imgcodecs/imgcodecs.hpp
/usr/include/opencv2/imgcodecs/imgcodecs_c.h
/usr/include/opencv2/imgcodecs/ios.h
/usr/include/opencv2/imgproc.hpp
/usr/include/opencv2/imgproc/detail/distortion_model.hpp
/usr/include/opencv2/imgproc/imgproc.hpp
/usr/include/opencv2/imgproc/imgproc_c.h
/usr/include/opencv2/imgproc/types_c.h
/usr/include/opencv2/ml.hpp
/usr/include/opencv2/ml/ml.hpp
/usr/include/opencv2/objdetect.hpp
/usr/include/opencv2/objdetect/detection_based_tracker.hpp
/usr/include/opencv2/objdetect/objdetect.hpp
/usr/include/opencv2/objdetect/objdetect_c.h
/usr/include/opencv2/opencv.hpp
/usr/include/opencv2/opencv_modules.hpp
/usr/include/opencv2/photo.hpp
/usr/include/opencv2/photo/cuda.hpp
/usr/include/opencv2/photo/photo.hpp
/usr/include/opencv2/photo/photo_c.h
/usr/include/opencv2/shape.hpp
/usr/include/opencv2/shape/emdL1.hpp
/usr/include/opencv2/shape/hist_cost.hpp
/usr/include/opencv2/shape/shape.hpp
/usr/include/opencv2/shape/shape_distance.hpp
/usr/include/opencv2/shape/shape_transformer.hpp
/usr/include/opencv2/stitching.hpp
/usr/include/opencv2/stitching/detail/autocalib.hpp
/usr/include/opencv2/stitching/detail/blenders.hpp
/usr/include/opencv2/stitching/detail/camera.hpp
/usr/include/opencv2/stitching/detail/exposure_compensate.hpp
/usr/include/opencv2/stitching/detail/matchers.hpp
/usr/include/opencv2/stitching/detail/motion_estimators.hpp
/usr/include/opencv2/stitching/detail/seam_finders.hpp
/usr/include/opencv2/stitching/detail/timelapsers.hpp
/usr/include/opencv2/stitching/detail/util.hpp
/usr/include/opencv2/stitching/detail/util_inl.hpp
/usr/include/opencv2/stitching/detail/warpers.hpp
/usr/include/opencv2/stitching/detail/warpers_inl.hpp
/usr/include/opencv2/stitching/warpers.hpp
/usr/include/opencv2/superres.hpp
/usr/include/opencv2/superres/optical_flow.hpp
/usr/include/opencv2/video.hpp
/usr/include/opencv2/video/background_segm.hpp
/usr/include/opencv2/video/tracking.hpp
/usr/include/opencv2/video/tracking_c.h
/usr/include/opencv2/video/video.hpp
/usr/include/opencv2/videoio.hpp
/usr/include/opencv2/videoio/cap_ios.h
/usr/include/opencv2/videoio/videoio.hpp
/usr/include/opencv2/videoio/videoio_c.h
/usr/include/opencv2/videostab.hpp
/usr/include/opencv2/videostab/deblurring.hpp
/usr/include/opencv2/videostab/fast_marching.hpp
/usr/include/opencv2/videostab/fast_marching_inl.hpp
/usr/include/opencv2/videostab/frame_source.hpp
/usr/include/opencv2/videostab/global_motion.hpp
/usr/include/opencv2/videostab/inpainting.hpp
/usr/include/opencv2/videostab/log.hpp
/usr/include/opencv2/videostab/motion_core.hpp
/usr/include/opencv2/videostab/motion_stabilizing.hpp
/usr/include/opencv2/videostab/optical_flow.hpp
/usr/include/opencv2/videostab/outlier_rejection.hpp
/usr/include/opencv2/videostab/ring_buffer.hpp
/usr/include/opencv2/videostab/stabilizer.hpp
/usr/include/opencv2/videostab/wobble_suppression.hpp
/usr/lib64/*.a
/usr/lib64/libopencv_calib3d.so
/usr/lib64/libopencv_core.so
/usr/lib64/libopencv_features2d.so
/usr/lib64/libopencv_flann.so
/usr/lib64/libopencv_highgui.so
/usr/lib64/libopencv_imgcodecs.so
/usr/lib64/libopencv_imgproc.so
/usr/lib64/libopencv_ml.so
/usr/lib64/libopencv_objdetect.so
/usr/lib64/libopencv_photo.so
/usr/lib64/libopencv_shape.so
/usr/lib64/libopencv_stitching.so
/usr/lib64/libopencv_superres.so
/usr/lib64/libopencv_video.so
/usr/lib64/libopencv_videoio.so
/usr/lib64/libopencv_videostab.so
/usr/lib64/pkgconfig/opencv.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopencv_calib3d.so.3.1
/usr/lib64/libopencv_calib3d.so.3.1.0
/usr/lib64/libopencv_core.so.3.1
/usr/lib64/libopencv_core.so.3.1.0
/usr/lib64/libopencv_features2d.so.3.1
/usr/lib64/libopencv_features2d.so.3.1.0
/usr/lib64/libopencv_flann.so.3.1
/usr/lib64/libopencv_flann.so.3.1.0
/usr/lib64/libopencv_highgui.so.3.1
/usr/lib64/libopencv_highgui.so.3.1.0
/usr/lib64/libopencv_imgcodecs.so.3.1
/usr/lib64/libopencv_imgcodecs.so.3.1.0
/usr/lib64/libopencv_imgproc.so.3.1
/usr/lib64/libopencv_imgproc.so.3.1.0
/usr/lib64/libopencv_ml.so.3.1
/usr/lib64/libopencv_ml.so.3.1.0
/usr/lib64/libopencv_objdetect.so.3.1
/usr/lib64/libopencv_objdetect.so.3.1.0
/usr/lib64/libopencv_photo.so.3.1
/usr/lib64/libopencv_photo.so.3.1.0
/usr/lib64/libopencv_shape.so.3.1
/usr/lib64/libopencv_shape.so.3.1.0
/usr/lib64/libopencv_stitching.so.3.1
/usr/lib64/libopencv_stitching.so.3.1.0
/usr/lib64/libopencv_superres.so.3.1
/usr/lib64/libopencv_superres.so.3.1.0
/usr/lib64/libopencv_video.so.3.1
/usr/lib64/libopencv_video.so.3.1.0
/usr/lib64/libopencv_videoio.so.3.1
/usr/lib64/libopencv_videoio.so.3.1.0
/usr/lib64/libopencv_videostab.so.3.1
/usr/lib64/libopencv_videostab.so.3.1.0

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*
