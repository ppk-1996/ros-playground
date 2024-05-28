FROM osrf/ros:noetic-desktop-full
ENV TZ=Australia/Brisbane

ARG DEBIAN_FRONTEND=noninteractive
ARG USER_ID=1000
ARG GROUP_ID=1000

# Install commonly-used development tools.
RUN apt-get update && apt-get install --yes \
    build-essential \
    clang-12 \
    clang-format-12 \
    cmake \
    g++ \
    gdb \
    git \
    nano \
    valgrind \
    vim

# Remap clang-12 and clang-format-12 to clang and clang-format, respectively.
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-12 100
RUN update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-12 100

# Additional installations
RUN apt-get update && apt-get install --yes \
    sudo \
    python-is-python3 \
    python3-catkin-tools \
    python3-pip \
    curl \
    iproute2 \
    iputils-ping \
    less \
    mesa-utils \
    net-tools \
    rsync \
    software-properties-common \
    tmux \
    tree \
    unzip \
    usbutils \
    wget \
    zip \
    zsh \
    terminator \
    liburdfdom-tools

# Create user 'developer' with USER_ID and GROUP_ID and add to sudo group
RUN groupadd -g ${GROUP_ID} developer && \
    useradd -m -s /bin/zsh -u ${USER_ID} -g developer developer && \
    adduser developer sudo

# Add user to sudoers file to disable sudo password prompt
RUN echo 'developer ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/developer

# Set up hostname in the container to avoid sudo warnings
RUN echo '127.0.0.1' >> /etc/hosts

ENV HOME /home/developer
ENV ROS_HOME /home/developer/.ros

# Switch to developer user
USER developer
WORKDIR /home/developer/ros-playground

# Set up terminal and 
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k && \
    git clone https://github.com/ingydotnet/git-subrepo ~/.local/bin/git-subrepo
COPY --chown=developer:developer configs/.* /home/developer/
COPY --chown=developer configs/terminator_config /home/developer/.config/terminator/config
