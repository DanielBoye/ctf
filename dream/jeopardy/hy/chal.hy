#!/usr/bin/env hy

(defn build-dict [a1 a2 a3 #* rest]
  (let [thisitem {(chr a1) (^ a2 a3)}]
    (if (len rest)
      (or (.update thisitem (build-dict #* rest)) thisitem)
      thisitem)))

(defn getByte [flag n]
  (let [index (* n 2)]
    (if (< index (len flag))
      (int (+ (get flag index) (get flag (+ index 1))) 16)
      "")))

(defn get-salt [flag] (lfor index (range 2 (// (len flag) 2) 3) (getByte flag index)))

(defn validate-salt [flag] (all (map (fn [x] (> x 200)) (get-salt flag))))

(defn get-multiplier [n]
  (if (in n "23456789")
    (int n)
    1))

(defn flag-to-dict [flag]
  (build-dict
    #* (lfor index (range 0 (// (len flag) 2))
      (getByte flag index))))

(defn dict-to-words [flagdict]
  (+ (.join "" (.keys flagdict)) "_" (.join "" (map chr (.values flagdict)))))

(defn validate-flag [flag targetProduct targetString]
  (assert (validate-salt flag))
  (assert (= (* #* (get-salt flag) #* (list (map get-multiplier flag))) targetProduct))
  (assert (= (dict-to-words (flag-to-dict flag)) targetString))
  flag)

(defn main []
  (try
    ; Test:
    (validate-flag "6c98f46fb1d876a3d06583f3" 60134327409746903040 "love_lisp")
    (print "Test passed")

    ; Challenge:
    (setv flag (input "Enter flag: "))
    (validate-flag flag 1342723557762272448000 "easy_flag")
    (print (+ "CTF{" flag "} is correct!"))

    (except [AssertionError]
      (print "That's not the flag, try again"))))


(main)
