;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun combinations (k lst)
  (if (zerop k)
      '(())
      (if (null lst)
          '()
          (append (mapcar (lambda (x) (cons (car lst) x))
                          (combinations (1- k) (cdr lst)))
                  (combinations k (cdr lst))))))
