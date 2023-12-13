;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun range-list (a b)
  (cond ((> a b) nil)
        ((= a b) (list a))
        (t (cons a (range-list (1+ a) b)))))
