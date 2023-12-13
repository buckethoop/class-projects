;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun decode (L)
  (if (null L)
    nil
    (let ((numCount (caar L)))
          (elem (cdr (car L))))
      (append (decodeSingCode numCount elem nil) (decode (cdr L)))
    )
  )
)
(defun decodeSingCode (count elem acc)
  (if (zerop count)
    acc
    (decodeSingCode (decf count) elem (cons elem acc))
  )
)
