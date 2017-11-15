{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_echo_service (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/bin"
libdir     = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/lib/x86_64-linux-ghc-8.0.2/echo-service-0.1.0.0-Cb4cOm8PIQx5UTeEunrLTD"
dynlibdir  = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/lib/x86_64-linux-ghc-8.0.2"
datadir    = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/share/x86_64-linux-ghc-8.0.2/echo-service-0.1.0.0"
libexecdir = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/libexec"
sysconfdir = "/home/ekkya/CS7NS1-Individual-task/.stack-work/install/x86_64-linux/lts-9.13/8.0.2/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "echo_service_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "echo_service_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "echo_service_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "echo_service_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "echo_service_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "echo_service_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
