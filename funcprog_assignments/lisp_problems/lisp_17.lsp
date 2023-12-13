;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun split-list (lst)
  (if (null lst)
      (cons '() '())
      (let ((first-elem (car lst))
            (rest (cdr lst))
            (less-equal '())
            (greater '()))
        (dolist (x rest)
          (if (> x first-elem)
              (setq greater (cons x greater))
              (setq less-equal (cons x less-equal))))
        (cons (cons first-elem less-equal) greater))))
