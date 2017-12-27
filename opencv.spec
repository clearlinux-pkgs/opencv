#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : opencv
Version  : 3.4.0
Release  : 44
URL      : https://github.com/opencv/opencv/archive/3.4.0.tar.gz
Source0  : https://github.com/opencv/opencv/archive/3.4.0.tar.gz
Summary  : Open Source Computer Vision Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 JasPer-2.0 LGPL-2.1 Libpng libtiff
Requires: opencv-bin
Requires: opencv-legacypython
Requires: opencv-python3
Requires: opencv-lib
Requires: opencv-data
Requires: opencv-python
BuildRequires : beautifulsoup4
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
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : numpy
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : tbb-dev
BuildRequires : v4l-utils-dev
BuildRequires : zlib-dev
Patch1: restrict.patch
Patch2: 0001-Add-basic-plumbing-for-AVX512-support.patch
Patch3: 0002-Provide-a-few-AVX512-optimized-functions-for-the-DNN.patch

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


%package extras
Summary: extras components for the opencv package.
Group: Default

%description extras
extras components for the opencv package.


%package legacypython
Summary: legacypython components for the opencv package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the opencv package.


%package lib
Summary: lib components for the opencv package.
Group: Libraries
Requires: opencv-data

%description lib
lib components for the opencv package.


%package python
Summary: python components for the opencv package.
Group: Default
Requires: opencv-legacypython
Requires: opencv-python3

%description python
python components for the opencv package.


%package python3
Summary: python3 components for the opencv package.
Group: Default
Requires: python3-core

%description python3
python3 components for the opencv package.


%prep
%setup -q -n opencv-3.4.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a opencv-3.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514304783
mkdir clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=ON -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=ON -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_SSE42=ON  -DWITH_TBB=ON -DWITH_OPENMP=ON -DWITH_VA=ON -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1  -DCPU_DISPATCH=AVX,AVX2,AVX512 -DLIB_SUFFIX= -DBUILD_EXAMPLES=ON -DINSTALL_C_EXAMPLES=ON -DINSTALL_PYTHON_EXAMPLES=ON
make VERBOSE=1  %{?_smp_mflags}
popd
mkdir clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell "
export CFLAGS="$CFLAGS -march=haswell"
export CXXFLAGS="$CXXFLAGS -march=haswell"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib/haswell -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=ON -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=ON -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_SSE42=ON  -DWITH_TBB=ON -DWITH_OPENMP=ON -DWITH_VA=ON -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1  -DCPU_DISPATCH=AVX,AVX2,AVX512 -DLIB_SUFFIX= -DBUILD_EXAMPLES=ON -DINSTALL_C_EXAMPLES=ON -DINSTALL_PYTHON_EXAMPLES=ON
make VERBOSE=1  %{?_smp_mflags}  || :
popd

%install
export SOURCE_DATE_EPOCH=1514304783
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/haswell/avx512_1
pushd clr-build-avx2
%make_install  || :
mv %{buildroot}/usr/lib64/*so* %{buildroot}/usr/lib64/haswell/ || :
popd
rm -f %{buildroot}/usr/bin/*
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/opencv_annotation
/usr/bin/opencv_createsamples
/usr/bin/opencv_interactive-calibration
/usr/bin/opencv_traincascade
/usr/bin/opencv_version
/usr/bin/opencv_visualisation

%files data
%defattr(-,root,root,-)
%exclude /usr/share/OpenCV/samples/cpp/3calibration.cpp
%exclude /usr/share/OpenCV/samples/cpp/application_trace.cpp
%exclude /usr/share/OpenCV/samples/cpp/autofocus.cpp
%exclude /usr/share/OpenCV/samples/cpp/bgfg_segm.cpp
%exclude /usr/share/OpenCV/samples/cpp/calibration.cpp
%exclude /usr/share/OpenCV/samples/cpp/camshiftdemo.cpp
%exclude /usr/share/OpenCV/samples/cpp/cloning_demo.cpp
%exclude /usr/share/OpenCV/samples/cpp/cloning_gui.cpp
%exclude /usr/share/OpenCV/samples/cpp/connected_components.cpp
%exclude /usr/share/OpenCV/samples/cpp/contours2.cpp
%exclude /usr/share/OpenCV/samples/cpp/convexhull.cpp
%exclude /usr/share/OpenCV/samples/cpp/cout_mat.cpp
%exclude /usr/share/OpenCV/samples/cpp/create_mask.cpp
%exclude /usr/share/OpenCV/samples/cpp/dbt_face_detection.cpp
%exclude /usr/share/OpenCV/samples/cpp/delaunay2.cpp
%exclude /usr/share/OpenCV/samples/cpp/demhist.cpp
%exclude /usr/share/OpenCV/samples/cpp/detect_blob.cpp
%exclude /usr/share/OpenCV/samples/cpp/detect_mser.cpp
%exclude /usr/share/OpenCV/samples/cpp/dft.cpp
%exclude /usr/share/OpenCV/samples/cpp/distrans.cpp
%exclude /usr/share/OpenCV/samples/cpp/drawing.cpp
%exclude /usr/share/OpenCV/samples/cpp/edge.cpp
%exclude /usr/share/OpenCV/samples/cpp/em.cpp
%exclude /usr/share/OpenCV/samples/cpp/facedetect.cpp
%exclude /usr/share/OpenCV/samples/cpp/facial_features.cpp
%exclude /usr/share/OpenCV/samples/cpp/falsecolor.cpp
%exclude /usr/share/OpenCV/samples/cpp/fback.cpp
%exclude /usr/share/OpenCV/samples/cpp/ffilldemo.cpp
%exclude /usr/share/OpenCV/samples/cpp/filestorage.cpp
%exclude /usr/share/OpenCV/samples/cpp/filestorage_base64.cpp
%exclude /usr/share/OpenCV/samples/cpp/fitellipse.cpp
%exclude /usr/share/OpenCV/samples/cpp/grabcut.cpp
%exclude /usr/share/OpenCV/samples/cpp/image.cpp
%exclude /usr/share/OpenCV/samples/cpp/image_alignment.cpp
%exclude /usr/share/OpenCV/samples/cpp/image_sequence.cpp
%exclude /usr/share/OpenCV/samples/cpp/imagelist_creator.cpp
%exclude /usr/share/OpenCV/samples/cpp/inpaint.cpp
%exclude /usr/share/OpenCV/samples/cpp/intelperc_capture.cpp
%exclude /usr/share/OpenCV/samples/cpp/kalman.cpp
%exclude /usr/share/OpenCV/samples/cpp/kmeans.cpp
%exclude /usr/share/OpenCV/samples/cpp/laplace.cpp
%exclude /usr/share/OpenCV/samples/cpp/letter_recog.cpp
%exclude /usr/share/OpenCV/samples/cpp/lkdemo.cpp
%exclude /usr/share/OpenCV/samples/cpp/logistic_regression.cpp
%exclude /usr/share/OpenCV/samples/cpp/lsd_lines.cpp
%exclude /usr/share/OpenCV/samples/cpp/mask_tmpl.cpp
%exclude /usr/share/OpenCV/samples/cpp/matchmethod_orb_akaze_brisk.cpp
%exclude /usr/share/OpenCV/samples/cpp/minarea.cpp
%exclude /usr/share/OpenCV/samples/cpp/morphology2.cpp
%exclude /usr/share/OpenCV/samples/cpp/neural_network.cpp
%exclude /usr/share/OpenCV/samples/cpp/npr_demo.cpp
%exclude /usr/share/OpenCV/samples/cpp/opencv_version.cpp
%exclude /usr/share/OpenCV/samples/cpp/openni_capture.cpp
%exclude /usr/share/OpenCV/samples/cpp/pca.cpp
%exclude /usr/share/OpenCV/samples/cpp/peopledetect.cpp
%exclude /usr/share/OpenCV/samples/cpp/phase_corr.cpp
%exclude /usr/share/OpenCV/samples/cpp/points_classifier.cpp
%exclude /usr/share/OpenCV/samples/cpp/polar_transforms.cpp
%exclude /usr/share/OpenCV/samples/cpp/segment_objects.cpp
%exclude /usr/share/OpenCV/samples/cpp/select3dobj.cpp
%exclude /usr/share/OpenCV/samples/cpp/shape_example.cpp
%exclude /usr/share/OpenCV/samples/cpp/smiledetect.cpp
%exclude /usr/share/OpenCV/samples/cpp/squares.cpp
%exclude /usr/share/OpenCV/samples/cpp/starter_imagelist.cpp
%exclude /usr/share/OpenCV/samples/cpp/stereo_calib.cpp
%exclude /usr/share/OpenCV/samples/cpp/stereo_match.cpp
%exclude /usr/share/OpenCV/samples/cpp/stitching.cpp
%exclude /usr/share/OpenCV/samples/cpp/stitching_detailed.cpp
%exclude /usr/share/OpenCV/samples/cpp/train_HOG.cpp
%exclude /usr/share/OpenCV/samples/cpp/train_svmsgd.cpp
%exclude /usr/share/OpenCV/samples/cpp/travelsalesman.cpp
%exclude /usr/share/OpenCV/samples/cpp/tree_engine.cpp
%exclude /usr/share/OpenCV/samples/cpp/tvl1_optical_flow.cpp
%exclude /usr/share/OpenCV/samples/cpp/videocapture_basic.cpp
%exclude /usr/share/OpenCV/samples/cpp/videocapture_starter.cpp
%exclude /usr/share/OpenCV/samples/cpp/videostab.cpp
%exclude /usr/share/OpenCV/samples/cpp/videowriter_basic.cpp
%exclude /usr/share/OpenCV/samples/cpp/warpPerspective_demo.cpp
%exclude /usr/share/OpenCV/samples/cpp/watershed.cpp
%exclude /usr/share/OpenCV/samples/dnn/caffe_googlenet.cpp
%exclude /usr/share/OpenCV/samples/dnn/faster_rcnn.cpp
%exclude /usr/share/OpenCV/samples/dnn/fcn_semsegm.cpp
%exclude /usr/share/OpenCV/samples/dnn/resnet_ssd_face.cpp
%exclude /usr/share/OpenCV/samples/dnn/squeezenet_halide.cpp
%exclude /usr/share/OpenCV/samples/dnn/ssd_mobilenet_object_detection.cpp
%exclude /usr/share/OpenCV/samples/dnn/ssd_object_detection.cpp
%exclude /usr/share/OpenCV/samples/dnn/tf_inception.cpp
%exclude /usr/share/OpenCV/samples/dnn/torch_enet.cpp
%exclude /usr/share/OpenCV/samples/dnn/yolo_object_detection.cpp
%exclude /usr/share/OpenCV/samples/gpu/alpha_comp.cpp
%exclude /usr/share/OpenCV/samples/gpu/bgfg_segm.cpp
%exclude /usr/share/OpenCV/samples/gpu/cascadeclassifier.cpp
%exclude /usr/share/OpenCV/samples/gpu/cascadeclassifier_nvidia_api.cpp
%exclude /usr/share/OpenCV/samples/gpu/driver_api_multi.cpp
%exclude /usr/share/OpenCV/samples/gpu/driver_api_stereo_multi.cpp
%exclude /usr/share/OpenCV/samples/gpu/farneback_optical_flow.cpp
%exclude /usr/share/OpenCV/samples/gpu/generalized_hough.cpp
%exclude /usr/share/OpenCV/samples/gpu/hog.cpp
%exclude /usr/share/OpenCV/samples/gpu/houghlines.cpp
%exclude /usr/share/OpenCV/samples/gpu/morphology.cpp
%exclude /usr/share/OpenCV/samples/gpu/multi.cpp
%exclude /usr/share/OpenCV/samples/gpu/opengl.cpp
%exclude /usr/share/OpenCV/samples/gpu/optical_flow.cpp
%exclude /usr/share/OpenCV/samples/gpu/opticalflow_nvidia_api.cpp
%exclude /usr/share/OpenCV/samples/gpu/pyrlk_optical_flow.cpp
%exclude /usr/share/OpenCV/samples/gpu/stereo_match.cpp
%exclude /usr/share/OpenCV/samples/gpu/stereo_multi.cpp
%exclude /usr/share/OpenCV/samples/gpu/super_resolution.cpp
%exclude /usr/share/OpenCV/samples/gpu/surf_keypoint_matcher.cpp
%exclude /usr/share/OpenCV/samples/gpu/video_reader.cpp
%exclude /usr/share/OpenCV/samples/gpu/video_writer.cpp
%exclude /usr/share/OpenCV/samples/tapi/bgfg_segm.cpp
%exclude /usr/share/OpenCV/samples/tapi/camshift.cpp
%exclude /usr/share/OpenCV/samples/tapi/clahe.cpp
%exclude /usr/share/OpenCV/samples/tapi/hog.cpp
%exclude /usr/share/OpenCV/samples/tapi/opencl_custom_kernel.cpp
%exclude /usr/share/OpenCV/samples/tapi/pyrlk_optical_flow.cpp
%exclude /usr/share/OpenCV/samples/tapi/squares.cpp
%exclude /usr/share/OpenCV/samples/tapi/tvl1_optical_flow.cpp
%exclude /usr/share/OpenCV/samples/tapi/ufacedetect.cpp
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
/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
/usr/share/OpenCV/lbpcascades/lbpcascade_silverware.xml
/usr/share/OpenCV/samples/python/_coverage.py
/usr/share/OpenCV/samples/python/_coverage.pyc
/usr/share/OpenCV/samples/python/_doc.py
/usr/share/OpenCV/samples/python/_doc.pyc
/usr/share/OpenCV/samples/python/asift.py
/usr/share/OpenCV/samples/python/asift.pyc
/usr/share/OpenCV/samples/python/browse.py
/usr/share/OpenCV/samples/python/browse.pyc
/usr/share/OpenCV/samples/python/calibrate.py
/usr/share/OpenCV/samples/python/calibrate.pyc
/usr/share/OpenCV/samples/python/camera_calibration_show_extrinsics.py
/usr/share/OpenCV/samples/python/camera_calibration_show_extrinsics.pyc
/usr/share/OpenCV/samples/python/camshift.py
/usr/share/OpenCV/samples/python/camshift.pyc
/usr/share/OpenCV/samples/python/coherence.py
/usr/share/OpenCV/samples/python/coherence.pyc
/usr/share/OpenCV/samples/python/color_histogram.py
/usr/share/OpenCV/samples/python/color_histogram.pyc
/usr/share/OpenCV/samples/python/common.py
/usr/share/OpenCV/samples/python/common.pyc
/usr/share/OpenCV/samples/python/contours.py
/usr/share/OpenCV/samples/python/contours.pyc
/usr/share/OpenCV/samples/python/deconvolution.py
/usr/share/OpenCV/samples/python/deconvolution.pyc
/usr/share/OpenCV/samples/python/demo.py
/usr/share/OpenCV/samples/python/demo.pyc
/usr/share/OpenCV/samples/python/dft.py
/usr/share/OpenCV/samples/python/dft.pyc
/usr/share/OpenCV/samples/python/digits.py
/usr/share/OpenCV/samples/python/digits.pyc
/usr/share/OpenCV/samples/python/digits_adjust.py
/usr/share/OpenCV/samples/python/digits_adjust.pyc
/usr/share/OpenCV/samples/python/digits_video.py
/usr/share/OpenCV/samples/python/digits_video.pyc
/usr/share/OpenCV/samples/python/distrans.py
/usr/share/OpenCV/samples/python/distrans.pyc
/usr/share/OpenCV/samples/python/edge.py
/usr/share/OpenCV/samples/python/edge.pyc
/usr/share/OpenCV/samples/python/facedetect.py
/usr/share/OpenCV/samples/python/facedetect.pyc
/usr/share/OpenCV/samples/python/feature_homography.py
/usr/share/OpenCV/samples/python/feature_homography.pyc
/usr/share/OpenCV/samples/python/find_obj.py
/usr/share/OpenCV/samples/python/find_obj.pyc
/usr/share/OpenCV/samples/python/fitline.py
/usr/share/OpenCV/samples/python/fitline.pyc
/usr/share/OpenCV/samples/python/floodfill.py
/usr/share/OpenCV/samples/python/floodfill.pyc
/usr/share/OpenCV/samples/python/gabor_threads.py
/usr/share/OpenCV/samples/python/gabor_threads.pyc
/usr/share/OpenCV/samples/python/gaussian_mix.py
/usr/share/OpenCV/samples/python/gaussian_mix.pyc
/usr/share/OpenCV/samples/python/grabcut.py
/usr/share/OpenCV/samples/python/grabcut.pyc
/usr/share/OpenCV/samples/python/hist.py
/usr/share/OpenCV/samples/python/hist.pyc
/usr/share/OpenCV/samples/python/houghcircles.py
/usr/share/OpenCV/samples/python/houghcircles.pyc
/usr/share/OpenCV/samples/python/houghlines.py
/usr/share/OpenCV/samples/python/houghlines.pyc
/usr/share/OpenCV/samples/python/inpaint.py
/usr/share/OpenCV/samples/python/inpaint.pyc
/usr/share/OpenCV/samples/python/kalman.py
/usr/share/OpenCV/samples/python/kalman.pyc
/usr/share/OpenCV/samples/python/kmeans.py
/usr/share/OpenCV/samples/python/kmeans.pyc
/usr/share/OpenCV/samples/python/lappyr.py
/usr/share/OpenCV/samples/python/lappyr.pyc
/usr/share/OpenCV/samples/python/letter_recog.py
/usr/share/OpenCV/samples/python/letter_recog.pyc
/usr/share/OpenCV/samples/python/lk_homography.py
/usr/share/OpenCV/samples/python/lk_homography.pyc
/usr/share/OpenCV/samples/python/lk_track.py
/usr/share/OpenCV/samples/python/lk_track.pyc
/usr/share/OpenCV/samples/python/logpolar.py
/usr/share/OpenCV/samples/python/logpolar.pyc
/usr/share/OpenCV/samples/python/morphology.py
/usr/share/OpenCV/samples/python/morphology.pyc
/usr/share/OpenCV/samples/python/mosse.py
/usr/share/OpenCV/samples/python/mosse.pyc
/usr/share/OpenCV/samples/python/mouse_and_match.py
/usr/share/OpenCV/samples/python/mouse_and_match.pyc
/usr/share/OpenCV/samples/python/mser.py
/usr/share/OpenCV/samples/python/mser.pyc
/usr/share/OpenCV/samples/python/opencv_version.py
/usr/share/OpenCV/samples/python/opencv_version.pyc
/usr/share/OpenCV/samples/python/opt_flow.py
/usr/share/OpenCV/samples/python/opt_flow.pyc
/usr/share/OpenCV/samples/python/peopledetect.py
/usr/share/OpenCV/samples/python/peopledetect.pyc
/usr/share/OpenCV/samples/python/plane_ar.py
/usr/share/OpenCV/samples/python/plane_ar.pyc
/usr/share/OpenCV/samples/python/plane_tracker.py
/usr/share/OpenCV/samples/python/plane_tracker.pyc
/usr/share/OpenCV/samples/python/squares.py
/usr/share/OpenCV/samples/python/squares.pyc
/usr/share/OpenCV/samples/python/stereo_match.py
/usr/share/OpenCV/samples/python/stereo_match.pyc
/usr/share/OpenCV/samples/python/texture_flow.py
/usr/share/OpenCV/samples/python/texture_flow.pyc
/usr/share/OpenCV/samples/python/tst_scene_render.py
/usr/share/OpenCV/samples/python/tst_scene_render.pyc
/usr/share/OpenCV/samples/python/turing.py
/usr/share/OpenCV/samples/python/turing.pyc
/usr/share/OpenCV/samples/python/video.py
/usr/share/OpenCV/samples/python/video.pyc
/usr/share/OpenCV/samples/python/video_threaded.py
/usr/share/OpenCV/samples/python/video_threaded.pyc
/usr/share/OpenCV/samples/python/video_v4l2.py
/usr/share/OpenCV/samples/python/video_v4l2.pyc
/usr/share/OpenCV/samples/python/watershed.py
/usr/share/OpenCV/samples/python/watershed.pyc
/usr/share/OpenCV/valgrind.supp
/usr/share/OpenCV/valgrind_3rdparty.supp

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
/usr/include/opencv2/core/cv_cpu_dispatch.h
/usr/include/opencv2/core/cv_cpu_helper.h
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
/usr/include/opencv2/core/hal/intrin_vsx.hpp
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
/usr/include/opencv2/core/ovx.hpp
/usr/include/opencv2/core/persistence.hpp
/usr/include/opencv2/core/ptr.inl.hpp
/usr/include/opencv2/core/saturate.hpp
/usr/include/opencv2/core/softfloat.hpp
/usr/include/opencv2/core/sse_utils.hpp
/usr/include/opencv2/core/traits.hpp
/usr/include/opencv2/core/types.hpp
/usr/include/opencv2/core/types_c.h
/usr/include/opencv2/core/utility.hpp
/usr/include/opencv2/core/utils/filesystem.hpp
/usr/include/opencv2/core/utils/logger.defines.hpp
/usr/include/opencv2/core/utils/logger.hpp
/usr/include/opencv2/core/utils/trace.hpp
/usr/include/opencv2/core/va_intel.hpp
/usr/include/opencv2/core/version.hpp
/usr/include/opencv2/core/vsx_utils.hpp
/usr/include/opencv2/core/wimage.hpp
/usr/include/opencv2/cvconfig.h
/usr/include/opencv2/dnn.hpp
/usr/include/opencv2/dnn/all_layers.hpp
/usr/include/opencv2/dnn/dict.hpp
/usr/include/opencv2/dnn/dnn.hpp
/usr/include/opencv2/dnn/dnn.inl.hpp
/usr/include/opencv2/dnn/layer.details.hpp
/usr/include/opencv2/dnn/layer.hpp
/usr/include/opencv2/dnn/shape_utils.hpp
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
/usr/include/opencv2/imgproc/hal/hal.hpp
/usr/include/opencv2/imgproc/hal/interface.h
/usr/include/opencv2/imgproc/imgproc.hpp
/usr/include/opencv2/imgproc/imgproc_c.h
/usr/include/opencv2/imgproc/types_c.h
/usr/include/opencv2/ml.hpp
/usr/include/opencv2/ml/ml.hpp
/usr/include/opencv2/ml/ml.inl.hpp
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
/usr/lib64/haswell/libopencv_calib3d.so
/usr/lib64/haswell/libopencv_core.so
/usr/lib64/haswell/libopencv_dnn.so
/usr/lib64/haswell/libopencv_features2d.so
/usr/lib64/haswell/libopencv_flann.so
/usr/lib64/haswell/libopencv_highgui.so
/usr/lib64/haswell/libopencv_imgcodecs.so
/usr/lib64/haswell/libopencv_imgproc.so
/usr/lib64/haswell/libopencv_ml.so
/usr/lib64/haswell/libopencv_objdetect.so
/usr/lib64/haswell/libopencv_photo.so
/usr/lib64/haswell/libopencv_shape.so
/usr/lib64/haswell/libopencv_stitching.so
/usr/lib64/haswell/libopencv_superres.so
/usr/lib64/haswell/libopencv_video.so
/usr/lib64/haswell/libopencv_videoio.so
/usr/lib64/haswell/libopencv_videostab.so
/usr/lib64/libopencv_calib3d.so
/usr/lib64/libopencv_core.so
/usr/lib64/libopencv_dnn.so
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

%files extras
%defattr(-,root,root,-)
/usr/share/OpenCV/samples/cpp/3calibration.cpp
/usr/share/OpenCV/samples/cpp/application_trace.cpp
/usr/share/OpenCV/samples/cpp/autofocus.cpp
/usr/share/OpenCV/samples/cpp/bgfg_segm.cpp
/usr/share/OpenCV/samples/cpp/calibration.cpp
/usr/share/OpenCV/samples/cpp/camshiftdemo.cpp
/usr/share/OpenCV/samples/cpp/cloning_demo.cpp
/usr/share/OpenCV/samples/cpp/cloning_gui.cpp
/usr/share/OpenCV/samples/cpp/connected_components.cpp
/usr/share/OpenCV/samples/cpp/contours2.cpp
/usr/share/OpenCV/samples/cpp/convexhull.cpp
/usr/share/OpenCV/samples/cpp/cout_mat.cpp
/usr/share/OpenCV/samples/cpp/create_mask.cpp
/usr/share/OpenCV/samples/cpp/dbt_face_detection.cpp
/usr/share/OpenCV/samples/cpp/delaunay2.cpp
/usr/share/OpenCV/samples/cpp/demhist.cpp
/usr/share/OpenCV/samples/cpp/detect_blob.cpp
/usr/share/OpenCV/samples/cpp/detect_mser.cpp
/usr/share/OpenCV/samples/cpp/dft.cpp
/usr/share/OpenCV/samples/cpp/distrans.cpp
/usr/share/OpenCV/samples/cpp/drawing.cpp
/usr/share/OpenCV/samples/cpp/edge.cpp
/usr/share/OpenCV/samples/cpp/em.cpp
/usr/share/OpenCV/samples/cpp/facedetect.cpp
/usr/share/OpenCV/samples/cpp/facial_features.cpp
/usr/share/OpenCV/samples/cpp/falsecolor.cpp
/usr/share/OpenCV/samples/cpp/fback.cpp
/usr/share/OpenCV/samples/cpp/ffilldemo.cpp
/usr/share/OpenCV/samples/cpp/filestorage.cpp
/usr/share/OpenCV/samples/cpp/filestorage_base64.cpp
/usr/share/OpenCV/samples/cpp/fitellipse.cpp
/usr/share/OpenCV/samples/cpp/grabcut.cpp
/usr/share/OpenCV/samples/cpp/image.cpp
/usr/share/OpenCV/samples/cpp/image_alignment.cpp
/usr/share/OpenCV/samples/cpp/image_sequence.cpp
/usr/share/OpenCV/samples/cpp/imagelist_creator.cpp
/usr/share/OpenCV/samples/cpp/inpaint.cpp
/usr/share/OpenCV/samples/cpp/intelperc_capture.cpp
/usr/share/OpenCV/samples/cpp/kalman.cpp
/usr/share/OpenCV/samples/cpp/kmeans.cpp
/usr/share/OpenCV/samples/cpp/laplace.cpp
/usr/share/OpenCV/samples/cpp/letter_recog.cpp
/usr/share/OpenCV/samples/cpp/lkdemo.cpp
/usr/share/OpenCV/samples/cpp/logistic_regression.cpp
/usr/share/OpenCV/samples/cpp/lsd_lines.cpp
/usr/share/OpenCV/samples/cpp/mask_tmpl.cpp
/usr/share/OpenCV/samples/cpp/matchmethod_orb_akaze_brisk.cpp
/usr/share/OpenCV/samples/cpp/minarea.cpp
/usr/share/OpenCV/samples/cpp/morphology2.cpp
/usr/share/OpenCV/samples/cpp/neural_network.cpp
/usr/share/OpenCV/samples/cpp/npr_demo.cpp
/usr/share/OpenCV/samples/cpp/opencv_version.cpp
/usr/share/OpenCV/samples/cpp/openni_capture.cpp
/usr/share/OpenCV/samples/cpp/pca.cpp
/usr/share/OpenCV/samples/cpp/peopledetect.cpp
/usr/share/OpenCV/samples/cpp/phase_corr.cpp
/usr/share/OpenCV/samples/cpp/points_classifier.cpp
/usr/share/OpenCV/samples/cpp/polar_transforms.cpp
/usr/share/OpenCV/samples/cpp/segment_objects.cpp
/usr/share/OpenCV/samples/cpp/select3dobj.cpp
/usr/share/OpenCV/samples/cpp/shape_example.cpp
/usr/share/OpenCV/samples/cpp/smiledetect.cpp
/usr/share/OpenCV/samples/cpp/squares.cpp
/usr/share/OpenCV/samples/cpp/starter_imagelist.cpp
/usr/share/OpenCV/samples/cpp/stereo_calib.cpp
/usr/share/OpenCV/samples/cpp/stereo_match.cpp
/usr/share/OpenCV/samples/cpp/stitching.cpp
/usr/share/OpenCV/samples/cpp/stitching_detailed.cpp
/usr/share/OpenCV/samples/cpp/train_HOG.cpp
/usr/share/OpenCV/samples/cpp/train_svmsgd.cpp
/usr/share/OpenCV/samples/cpp/travelsalesman.cpp
/usr/share/OpenCV/samples/cpp/tree_engine.cpp
/usr/share/OpenCV/samples/cpp/tvl1_optical_flow.cpp
/usr/share/OpenCV/samples/cpp/videocapture_basic.cpp
/usr/share/OpenCV/samples/cpp/videocapture_starter.cpp
/usr/share/OpenCV/samples/cpp/videostab.cpp
/usr/share/OpenCV/samples/cpp/videowriter_basic.cpp
/usr/share/OpenCV/samples/cpp/warpPerspective_demo.cpp
/usr/share/OpenCV/samples/cpp/watershed.cpp
/usr/share/OpenCV/samples/dnn/caffe_googlenet.cpp
/usr/share/OpenCV/samples/dnn/faster_rcnn.cpp
/usr/share/OpenCV/samples/dnn/fcn_semsegm.cpp
/usr/share/OpenCV/samples/dnn/resnet_ssd_face.cpp
/usr/share/OpenCV/samples/dnn/squeezenet_halide.cpp
/usr/share/OpenCV/samples/dnn/ssd_mobilenet_object_detection.cpp
/usr/share/OpenCV/samples/dnn/ssd_object_detection.cpp
/usr/share/OpenCV/samples/dnn/tf_inception.cpp
/usr/share/OpenCV/samples/dnn/torch_enet.cpp
/usr/share/OpenCV/samples/dnn/yolo_object_detection.cpp
/usr/share/OpenCV/samples/gpu/alpha_comp.cpp
/usr/share/OpenCV/samples/gpu/bgfg_segm.cpp
/usr/share/OpenCV/samples/gpu/cascadeclassifier.cpp
/usr/share/OpenCV/samples/gpu/cascadeclassifier_nvidia_api.cpp
/usr/share/OpenCV/samples/gpu/driver_api_multi.cpp
/usr/share/OpenCV/samples/gpu/driver_api_stereo_multi.cpp
/usr/share/OpenCV/samples/gpu/farneback_optical_flow.cpp
/usr/share/OpenCV/samples/gpu/generalized_hough.cpp
/usr/share/OpenCV/samples/gpu/hog.cpp
/usr/share/OpenCV/samples/gpu/houghlines.cpp
/usr/share/OpenCV/samples/gpu/morphology.cpp
/usr/share/OpenCV/samples/gpu/multi.cpp
/usr/share/OpenCV/samples/gpu/opengl.cpp
/usr/share/OpenCV/samples/gpu/optical_flow.cpp
/usr/share/OpenCV/samples/gpu/opticalflow_nvidia_api.cpp
/usr/share/OpenCV/samples/gpu/pyrlk_optical_flow.cpp
/usr/share/OpenCV/samples/gpu/stereo_match.cpp
/usr/share/OpenCV/samples/gpu/stereo_multi.cpp
/usr/share/OpenCV/samples/gpu/super_resolution.cpp
/usr/share/OpenCV/samples/gpu/surf_keypoint_matcher.cpp
/usr/share/OpenCV/samples/gpu/video_reader.cpp
/usr/share/OpenCV/samples/gpu/video_writer.cpp
/usr/share/OpenCV/samples/tapi/bgfg_segm.cpp
/usr/share/OpenCV/samples/tapi/camshift.cpp
/usr/share/OpenCV/samples/tapi/clahe.cpp
/usr/share/OpenCV/samples/tapi/hog.cpp
/usr/share/OpenCV/samples/tapi/opencl_custom_kernel.cpp
/usr/share/OpenCV/samples/tapi/pyrlk_optical_flow.cpp
/usr/share/OpenCV/samples/tapi/squares.cpp
/usr/share/OpenCV/samples/tapi/tvl1_optical_flow.cpp
/usr/share/OpenCV/samples/tapi/ufacedetect.cpp

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libopencv_calib3d.so.3.4
/usr/lib64/haswell/libopencv_calib3d.so.3.4.0
/usr/lib64/haswell/libopencv_core.so.3.4
/usr/lib64/haswell/libopencv_core.so.3.4.0
/usr/lib64/haswell/libopencv_dnn.so.3.4
/usr/lib64/haswell/libopencv_dnn.so.3.4.0
/usr/lib64/haswell/libopencv_features2d.so.3.4
/usr/lib64/haswell/libopencv_features2d.so.3.4.0
/usr/lib64/haswell/libopencv_flann.so.3.4
/usr/lib64/haswell/libopencv_flann.so.3.4.0
/usr/lib64/haswell/libopencv_highgui.so.3.4
/usr/lib64/haswell/libopencv_highgui.so.3.4.0
/usr/lib64/haswell/libopencv_imgcodecs.so.3.4
/usr/lib64/haswell/libopencv_imgcodecs.so.3.4.0
/usr/lib64/haswell/libopencv_imgproc.so.3.4
/usr/lib64/haswell/libopencv_imgproc.so.3.4.0
/usr/lib64/haswell/libopencv_ml.so.3.4
/usr/lib64/haswell/libopencv_ml.so.3.4.0
/usr/lib64/haswell/libopencv_objdetect.so.3.4
/usr/lib64/haswell/libopencv_objdetect.so.3.4.0
/usr/lib64/haswell/libopencv_photo.so.3.4
/usr/lib64/haswell/libopencv_photo.so.3.4.0
/usr/lib64/haswell/libopencv_shape.so.3.4
/usr/lib64/haswell/libopencv_shape.so.3.4.0
/usr/lib64/haswell/libopencv_stitching.so.3.4
/usr/lib64/haswell/libopencv_stitching.so.3.4.0
/usr/lib64/haswell/libopencv_superres.so.3.4
/usr/lib64/haswell/libopencv_superres.so.3.4.0
/usr/lib64/haswell/libopencv_video.so.3.4
/usr/lib64/haswell/libopencv_video.so.3.4.0
/usr/lib64/haswell/libopencv_videoio.so.3.4
/usr/lib64/haswell/libopencv_videoio.so.3.4.0
/usr/lib64/haswell/libopencv_videostab.so.3.4
/usr/lib64/haswell/libopencv_videostab.so.3.4.0
/usr/lib64/libopencv_calib3d.so.3.4
/usr/lib64/libopencv_calib3d.so.3.4.0
/usr/lib64/libopencv_core.so.3.4
/usr/lib64/libopencv_core.so.3.4.0
/usr/lib64/libopencv_dnn.so.3.4
/usr/lib64/libopencv_dnn.so.3.4.0
/usr/lib64/libopencv_features2d.so.3.4
/usr/lib64/libopencv_features2d.so.3.4.0
/usr/lib64/libopencv_flann.so.3.4
/usr/lib64/libopencv_flann.so.3.4.0
/usr/lib64/libopencv_highgui.so.3.4
/usr/lib64/libopencv_highgui.so.3.4.0
/usr/lib64/libopencv_imgcodecs.so.3.4
/usr/lib64/libopencv_imgcodecs.so.3.4.0
/usr/lib64/libopencv_imgproc.so.3.4
/usr/lib64/libopencv_imgproc.so.3.4.0
/usr/lib64/libopencv_ml.so.3.4
/usr/lib64/libopencv_ml.so.3.4.0
/usr/lib64/libopencv_objdetect.so.3.4
/usr/lib64/libopencv_objdetect.so.3.4.0
/usr/lib64/libopencv_photo.so.3.4
/usr/lib64/libopencv_photo.so.3.4.0
/usr/lib64/libopencv_shape.so.3.4
/usr/lib64/libopencv_shape.so.3.4.0
/usr/lib64/libopencv_stitching.so.3.4
/usr/lib64/libopencv_stitching.so.3.4.0
/usr/lib64/libopencv_superres.so.3.4
/usr/lib64/libopencv_superres.so.3.4.0
/usr/lib64/libopencv_video.so.3.4
/usr/lib64/libopencv_video.so.3.4.0
/usr/lib64/libopencv_videoio.so.3.4
/usr/lib64/libopencv_videoio.so.3.4.0
/usr/lib64/libopencv_videostab.so.3.4
/usr/lib64/libopencv_videostab.so.3.4.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
