{-# LANGUAGE DataKinds       #-}
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE TypeOperators   #-}
module Lib
    ( startApp
    , app
    ) where

import Data.Aeson
import Data.Aeson.TH
import Network.Wai
import Network.Wai.Handler.Warp
import Servant
import Data.Char

data User = User
  { userId :: Int
  , userFirstName :: String
  , userLastName  :: String 
  } deriving (Eq, Show)

$(deriveJSON defaultOptions ''User)

main :: IO ()
main = do
     putStrLn "Enter a line of text for test 1:"
     s <- getLine
     let bigFirstName = map toUpper s
         bigLastName = map toUpper s
     putStrLn $ "hey " ++ bigFirstName ++ " " ++ bigLastName ++ ", how are you?" 

type API = "users" :> Get '[JSON] [User]

startApp :: IO ()
startApp = do
     putStrLn "Enter a line of text for test 1:"
     s <- getLine
     let bigFirstName = map toUpper s
     putStrLn $ "hey " ++ bigFirstName ++ " " ++ ", how are you?"
     run 8081 app 

app :: Application
app = serve api server

api :: Proxy API
api = Proxy

server :: Server API
server = return users

users :: [User]
users = [ User 1 "Isaac" "Newton"
        , User 2 "Albert" "Einstein"
       ]
